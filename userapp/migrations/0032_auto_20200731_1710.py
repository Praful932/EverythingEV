# Generated by Django 3.0.5 on 2020-07-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0031_auto_20200724_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargepooler',
            name='city',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='chargepooler',
            name='cost',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='chargepooler',
            name='local_area',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='chargepooler',
            name='ph_no',
            field=models.CharField(max_length=13),
        ),
    ]
