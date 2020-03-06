# Generated by Django 2.2 on 2020-03-06 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_chargingstation_available_ports'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingStationRecord',
            fields=[
                ('cs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='userapp.ChargingStation')),
                ('elec_kwh', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
