from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    Problem = models.CharField(max_length=100, default='')
    Additional_Info = models.TextField(default='')
    user_loc = models.CharField(max_length=100, default='Default Location')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request #{self.pk} - {self.Problem}"


class Message(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title