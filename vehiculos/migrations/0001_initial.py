# Generated by Django 2.0.4 on 2018-04-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('submarca', models.CharField(max_length=30)),
                ('clase', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('modelo', models.IntegerField()),
                ('numero_serie', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('apodo', models.CharField(blank=True, max_length=10, null=True)),
                ('kilometraje', models.IntegerField()),
                ('status', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupado', 'Ocupado'), ('En taller', 'En taller')], default='Disponible', max_length=10)),
            ],
        ),
    ]