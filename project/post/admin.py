from django.contrib import admin

# Register your models here.
from post.models import Request, Message

admin.site.register(Request)
admin.site.register(Message)