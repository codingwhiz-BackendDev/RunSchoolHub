# Generated by Django 5.0 on 2024-08-08 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_alter_post_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
            ],
        ),
    ]