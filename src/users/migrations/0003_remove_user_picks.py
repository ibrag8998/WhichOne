# Generated by Django 3.0.6 on 2020-06-06 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200602_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picks',
        ),
    ]