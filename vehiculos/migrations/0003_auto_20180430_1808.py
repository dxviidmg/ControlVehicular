# Generated by Django 2.0.4 on 2018-04-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_auto_20180430_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aseguradora',
            name='Nombre',
            field=models.CharField(max_length=30),
        ),
    ]