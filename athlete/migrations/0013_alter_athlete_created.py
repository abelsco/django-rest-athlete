# Generated by Django 4.0.3 on 2022-04-06 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0012_athlete_created_athlete_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]