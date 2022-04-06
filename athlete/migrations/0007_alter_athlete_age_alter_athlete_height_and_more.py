# Generated by Django 4.0.3 on 2022-04-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athlete', '0006_alter_athlete_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
