# Generated by Django 4.0.3 on 2022-04-06 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0011_alter_athlete_options_remove_athlete_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='athlete',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
