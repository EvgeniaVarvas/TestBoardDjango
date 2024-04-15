from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Register, EmailVerification, MyLoginView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('verify_email/<uidb64>/<token>/', EmailVerification.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email'),
    path('register/', Register.as_view(), name='register'),
    path('invalid_token/', TemplateView.as_view(template_name='registration/invalid_token.html'), name='invalid_token'),
]



