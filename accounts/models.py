from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    industry = models.CharField(max_length=100, blank=True)
    experience = models.IntegerField(default=0)
    credits = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.email} - {self.industry}"