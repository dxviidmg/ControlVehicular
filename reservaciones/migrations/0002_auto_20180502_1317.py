# Generated by Django 2.0.4 on 2018-05-02 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='revision',
            name='creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
