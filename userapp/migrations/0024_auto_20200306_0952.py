# Generated by Django 2.2 on 2020-03-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0023_auto_20200306_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=18.480337, max_digits=9),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=73.839854, max_digits=9),
        ),
    ]
