from django.db import models

from django_random_queryset import RandomManager


class Title(models.Model):
    text = models.CharField(max_length=255, unique=True)
    picks = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)

    objects = RandomManager()

    def __str__(self):
        return self.text
