# Generated by Django 3.0.6 on 2020-06-06 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('titles', '0002_auto_20200606_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to=settings.AUTH_USER_MODEL),
        ),
    ]
