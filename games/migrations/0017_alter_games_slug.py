# Generated by Django 4.0.3 on 2022-04-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_alter_games_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='slug',
            field=models.SlugField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
