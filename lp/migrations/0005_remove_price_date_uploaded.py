# Generated by Django 3.0 on 2020-01-21 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0004_auto_20200121_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='date_uploaded',
        ),
    ]
