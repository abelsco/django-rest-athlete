# Generated by Django 4.0.3 on 2022-04-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_games_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='games',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='games',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
