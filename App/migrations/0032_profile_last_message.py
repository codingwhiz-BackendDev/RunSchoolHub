# Generated by Django 5.0 on 2024-08-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0031_lastmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_message',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
