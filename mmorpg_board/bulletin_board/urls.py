from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostView, PostDetail, PostCreate


urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)