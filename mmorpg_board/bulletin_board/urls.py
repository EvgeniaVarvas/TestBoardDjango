from django.urls import path
from .views import PostView, PostDetail


urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
