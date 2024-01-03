from django.contrib.auth import get_user_model
from django.db import models

from ..constants import DEFAULT_USER_AVATAR


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar_url = models.URLField(blank=False, null=False, default=DEFAULT_USER_AVATAR)
