# Generated by Django 4.0.3 on 2022-04-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0009_alter_athlete_noc'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
