# Generated by Django 4.0.3 on 2022-04-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('sport', models.CharField(max_length=30)),
                ('games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.games')),
            ],
        ),
    ]