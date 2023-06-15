from django.urls import path
from post.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name= 'list-create-Request'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='read-update-delete-Request')
]