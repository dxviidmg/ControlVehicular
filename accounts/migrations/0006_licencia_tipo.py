# Generated by Django 2.0.4 on 2018-05-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180509_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='licencia',
            name='tipo',
            field=models.CharField(default='A', max_length=1),
        ),
    ]