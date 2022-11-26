# Generated by Django 3.0.5 on 2020-06-13 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0020_survey_means_of_travel"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
