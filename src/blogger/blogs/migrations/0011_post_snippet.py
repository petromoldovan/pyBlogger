# Generated by Django 3.1.4 on 2020-12-20 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20201220_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='blog snippet', max_length=255),
        ),
    ]
