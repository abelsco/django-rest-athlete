# Generated by Django 4.0.3 on 2022-04-06 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_games_options_remove_games_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='name',
        ),
    ]