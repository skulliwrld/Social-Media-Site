# Generated by Django 4.1.1 on 2022-10-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='R.png', upload_to='profile_images'),
        ),
    ]
