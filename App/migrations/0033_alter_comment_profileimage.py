# Generated by Django 5.0 on 2024-08-07 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0032_profile_last_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profileimage',
            field=models.ImageField(default='blank.png', upload_to='comment'),
        ),
    ]