# Generated by Django 2.2 on 2020-03-08 07:07

from django.db import migrations, models
import django.db.models.deletion
import userapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=userapp.models.randomdate)),
                ('t0', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t1', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t2', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t3', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t4', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t5', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t6', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t7', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t8', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t9', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t10', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t11', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t12', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t13', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t14', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t15', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t16', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t17', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t18', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t19', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t20', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t21', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t22', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t23', models.IntegerField(default=userapp.models.randomvehicles)),
                ('t24', models.IntegerField(default=userapp.models.randomvehicles)),
                ('cs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ChargingStation')),
            ],
        ),
    ]
