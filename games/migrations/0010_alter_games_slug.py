# Generated by Django 4.0.3 on 2022-04-06 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_games_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='slug',
            field=models.SlugField(default='', primary_key=True, serialize=False),
        ),
    ]
