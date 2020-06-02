# Generated by Django 3.0.6 on 2020-06-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True)),
                ('picks', models.IntegerField(default=0)),
                ('appearances', models.IntegerField(default=0)),
            ],
        ),
    ]
