# Generated by Django 4.2.6 on 2023-11-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='users/profile_images'),
        ),
    ]