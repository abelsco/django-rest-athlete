# Generated by Django 4.0.3 on 2022-04-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_alter_games_created_alter_games_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='slug',
            field=models.CharField(default='', max_length=255, primary_key=True, serialize=False),
        ),
    ]