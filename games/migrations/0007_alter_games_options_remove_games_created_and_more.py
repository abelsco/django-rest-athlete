# Generated by Django 4.0.3 on 2022-04-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_remove_games_slug_games_slug_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ('-slug',)},
        ),
        migrations.RemoveField(
            model_name='games',
            name='created',
        ),
        migrations.RemoveField(
            model_name='games',
            name='slug_id',
        ),
        migrations.RemoveField(
            model_name='games',
            name='updated',
        ),
        migrations.AddField(
            model_name='games',
            name='slug',
            field=models.SlugField(default='', serialize=False),
        ),
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=13),
        ),
    ]