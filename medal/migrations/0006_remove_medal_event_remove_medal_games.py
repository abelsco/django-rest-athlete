# Generated by Django 4.0.3 on 2022-04-05 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medal', '0005_alter_medal_unique_together_medal_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medal',
            name='event',
        ),
        migrations.RemoveField(
            model_name='medal',
            name='games',
        ),
    ]