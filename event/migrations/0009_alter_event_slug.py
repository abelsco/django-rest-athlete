# Generated by Django 4.0.3 on 2022-04-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', max_length=150, unique=True),
        ),
    ]
