# Generated by Django 4.0.3 on 2022-04-06 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0016_alter_athlete_created_alter_athlete_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ('-id',), 'verbose_name': 'Athlete', 'verbose_name_plural': 'Athletes'},
        ),
    ]
