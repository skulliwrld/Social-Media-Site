# Generated by Django 4.1.1 on 2022-10-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0006_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(upload_to='profile_images'),
        ),
    ]
