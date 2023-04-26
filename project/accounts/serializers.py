from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from djoser.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from accounts.models import Profile


User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    first_name = serializers.CharField(max_length = 225, write_only=True)
    last_name = serializers.CharField(max_length = 225, write_only=True)
    birthdate = serializers.DateField(write_only=True)
    gender = serializers.CharField(max_length = 6, write_only = True)
    username = serializers.CharField(max_length = 225, write_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "gender",
            "username"
        )

    def clean_profile_data(self,validated_data):
        return{
            'birthdate' : validated_data.get('birthdate', ''),
            'gender' : validated_data.get('gender', '')
        }
    
    def clean_user_data(self,validated_data):
        return{
            'first_name' : validated_data.get('first_name', ''),
            'last_name' : validated_data.get('last_name', ''),
            'email' : validated_data.get('email', ''),
            'password' : validated_data.get('password',''),
            'username' : validated_data.get('username', '')
        }

    def validate(self, attrs):
        user_data = self.clean_user_data(attrs)
        user = User(**user_data)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user_data = self.clean_user_data(validated_data)
            user = User.objects.create_user(**user_data)
            Profile.objects.create(user=user, **self.clean_profile_data(validated_data=validated_data))
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user
