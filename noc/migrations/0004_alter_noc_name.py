# Generated by Django 4.0.3 on 2022-04-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0003_remove_noc_id_alter_noc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noc',
            name='name',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, unique=True),
        ),
    ]
