# Generated by Django 4.1.1 on 2022-10-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='504-5040528_empty-profile-picture-png-transparent-png.png', upload_to='profile_images'),
        ),
    ]
