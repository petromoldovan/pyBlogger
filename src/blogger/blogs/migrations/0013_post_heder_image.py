# Generated by Django 3.1.4 on 2020-12-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_auto_20201220_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heder_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
