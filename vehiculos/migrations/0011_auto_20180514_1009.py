# Generated by Django 2.0.4 on 2018-05-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0010_auto_20180514_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seguro',
            old_name='iniciso',
            new_name='inciso',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='nombre',
            field=models.CharField(max_length=10),
        ),
    ]