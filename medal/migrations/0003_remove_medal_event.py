# Generated by Django 4.0.3 on 2022-04-05 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medal', '0002_alter_medal_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medal',
            name='event',
        ),
    ]