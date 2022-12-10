# Generated by Django 2.2 on 2020-03-09 08:09

from django.db import migrations, models
import django.db.models.deletion
import userapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0004_chargingstationweekly"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChargePooler",
            fields=[
                (
                    "consumer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="userapp.Consumer",
                    ),
                ),
                ("city", models.CharField(default=userapp.models.city, max_length=25)),
                (
                    "local_area",
                    models.CharField(default=userapp.models.sub, max_length=25),
                ),
                (
                    "ph_no",
                    models.CharField(default=userapp.models.phone, max_length=13),
                ),
                ("cost", models.CharField(default=userapp.models.price, max_length=25)),
                ("normal_port", models.BooleanField(default=True)),
                ("fast_port", models.BooleanField(default=False)),
            ],
        ),
    ]
