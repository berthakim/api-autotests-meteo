# Generated by Django 3.2.3 on 2021-11-30 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arkeo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meteostation',
            name='created',
        ),
    ]
