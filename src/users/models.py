from django.db import models
from django.contrib.auth.models import AbstractUser

from titles.models import Title


class User(AbstractUser):
    email = models.EmailField(unique=True)
    picks = models.ManyToManyField(Title, 'users')
