# Generated by Django 5.0 on 2024-09-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0043_alter_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.FileField(null=True, upload_to='Image'),
        ),
    ]