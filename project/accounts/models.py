from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6)

from django.core.validators import MinValueValidator, MaxValueValidator

class Request(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('ongoing', 'Ongoing'),
        ('complete', 'Complete'),
    )

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    accepter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='accepted_requests')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requester_rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1, message='Rating must be at least 1.'),
            MaxValueValidator(5, message='Rating cannot exceed 5.'),
        ]
    )
    accepter_rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1, message='Rating must be at least 1.'),
            MaxValueValidator(5, message='Rating cannot exceed 5.'),
        ]
    )


class Message(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title