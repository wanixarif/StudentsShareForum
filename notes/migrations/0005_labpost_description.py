# Generated by Django 3.0.4 on 2020-03-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20200321_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='labpost',
            name='description',
            field=models.TextField(default=' ', max_length=200),
        ),
    ]
