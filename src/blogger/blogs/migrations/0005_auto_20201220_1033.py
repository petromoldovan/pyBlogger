# Generated by Django 3.1.4 on 2020-12-20 10:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_post_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid5, editable=False, unique=True),
        ),
    ]
