# Generated by Django 3.0.4 on 2020-03-24 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0018_auto_20200324_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepost',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
