# Generated by Django 4.0.3 on 2022-04-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noc', '0005_alter_noc_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noc',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='noc',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='noc',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
