# Generated by Django 3.0.5 on 2020-06-13 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0022_vehicle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='vehicle_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Vehicle'),
        ),
    ]
