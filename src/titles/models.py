from django.db import models

from django_random_queryset import RandomManager

from users.models import User


class Title(models.Model):
    text = models.CharField(max_length=255, unique=True)
    picks = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)
    users = models.ManyToManyField(User, 'picks')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='titles',
    )

    objects = RandomManager()

    @property
    def winrate(self):
        return round(self.picks / self.appearances * 100, 1)

    def __str__(self):
        return self.text
