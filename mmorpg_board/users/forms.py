from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm as DjangoAuthenticationForm,
    UserCreationForm as DjangoUserCreationForm)
from django.utils.translation import gettext_lazy as _

from users.utils import send_email_verification

User = get_user_model()


class AuthenticationForm(DjangoAuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )
            if not self.user_cache.email_verified:
                send_email_verification(self.request, self.user_cache)
                raise forms.ValidationError("Email is not verified", code='email_not_verified')
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}))

    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
