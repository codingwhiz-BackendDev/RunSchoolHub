# Generated by Django 5.0 on 2024-09-12 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0040_message_image_message_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='video',
        ),
    ]
