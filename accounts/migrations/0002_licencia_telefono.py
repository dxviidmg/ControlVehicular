# Generated by Django 2.0.4 on 2018-05-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
