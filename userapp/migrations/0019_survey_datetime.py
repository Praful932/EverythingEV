# Generated by Django 3.0.5 on 2020-06-08 06:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0018_survey"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="datetime",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
