# Generated by Django 3.0.5 on 2020-07-16 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0025_auto_20200715_2109"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vehicle",
            old_name="horsepower",
            new_name="battery_capacity",
        ),
    ]
