from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = models.CharField(max_length=45, blank=False, null=False, unique=True)
    email = models.EmailField(_("e-mail address"), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]
