# Generated by Django 4.0.3 on 2022-04-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0015_alter_athlete_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
