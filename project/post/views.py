from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.models import Request
from post.serializers import PostSerializers

class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializers
    queryset = Request.objects.all()

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializers
    queryset = Request.objects.all()