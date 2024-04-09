from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ("username",)
