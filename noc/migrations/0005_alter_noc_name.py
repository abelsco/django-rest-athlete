# Generated by Django 4.0.3 on 2022-04-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0004_alter_noc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noc',
            name='name',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
