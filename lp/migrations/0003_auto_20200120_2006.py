# Generated by Django 3.0 on 2020-01-20 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0002_auto_20200120_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='date_uploaded',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
