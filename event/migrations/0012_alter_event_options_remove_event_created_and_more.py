# Generated by Django 4.0.3 on 2022-04-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_remove_event_slug_event_slug_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-slug',)},
        ),
        migrations.RemoveField(
            model_name='event',
            name='created',
        ),
        migrations.RemoveField(
            model_name='event',
            name='slug_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated',
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', max_length=255, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
