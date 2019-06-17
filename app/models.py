from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core import validators
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    Token.objects.get_or_create(user=instance)

#removing the user
def remove_user(strategy, entries, *args, **kwargs):
    user = kwargs.get('user')
    user.is_active = False
    user.save()
