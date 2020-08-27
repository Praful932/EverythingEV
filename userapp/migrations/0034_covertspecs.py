# Generated by Django 3.0.5 on 2020-08-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0033_user_convert_specs'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovertSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_capacity', models.IntegerField(default=0)),
                ('range_in_kms', models.IntegerField(default=0)),
                ('battery_warranty', models.IntegerField(default=0)),
                ('Pricing', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=3)),
                ('company', models.CharField(max_length=25)),
            ],
        ),
    ]
