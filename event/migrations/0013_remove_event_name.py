# Generated by Django 4.0.3 on 2022-04-06 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_alter_event_options_remove_event_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
    ]
