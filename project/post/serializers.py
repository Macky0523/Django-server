from rest_framework import serializers
from post.models import Request,Message

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
