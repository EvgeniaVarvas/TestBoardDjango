from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'),
                              unique=True,
                              error_messages={'unique': _('A user with that email already exists.')},
                              blank=False)
    email_verified = models.BooleanField(default=False)
