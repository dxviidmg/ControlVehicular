# Generated by Django 2.0.4 on 2018-10-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_licencia_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencia',
            name='tipo',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=1),
        ),
    ]
