# Generated by Django 4.2.6 on 2023-10-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='users/profile.images'),
        ),
    ]
