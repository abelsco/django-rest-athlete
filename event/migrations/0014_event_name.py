# Generated by Django 4.0.3 on 2022-04-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_remove_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]