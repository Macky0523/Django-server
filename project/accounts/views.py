from django.shortcuts import render

from .models import Request

def my_view(request):
    # Example usage:
    requests = Request.objects.all()  # Retrieve all requests
    # ...
