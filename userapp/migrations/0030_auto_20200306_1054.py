# Generated by Django 2.2 on 2020-03-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0029_auto_20200306_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=18.522902, max_digits=9),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=73.830078, max_digits=9),
        ),
    ]
