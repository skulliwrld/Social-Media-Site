# Generated by Django 4.1.1 on 2022-10-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0008_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
