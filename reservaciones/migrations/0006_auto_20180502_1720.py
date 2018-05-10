# Generated by Django 2.0.4 on 2018-05-02 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservaciones', '0005_auto_20180502_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculos.Vehiculo'),
        ),
    ]