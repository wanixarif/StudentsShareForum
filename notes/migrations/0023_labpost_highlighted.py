# Generated by Django 3.0.4 on 2020-04-29 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0022_labpost_linenos'),
    ]

    operations = [
        migrations.AddField(
            model_name='labpost',
            name='highlighted',
            field=models.TextField(default='Null'),
            preserve_default=False,
        ),
    ]
