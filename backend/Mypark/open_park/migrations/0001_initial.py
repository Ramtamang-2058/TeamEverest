# Generated by Django 4.2.5 on 2023-09-15 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import open_park.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('car_slot', models.IntegerField(blank=True, null=True)),
                ('bike_slot', models.IntegerField(blank=True, null=True)),
                ('car_charge', models.IntegerField(blank=True, null=True)),
                ('bike_charge', models.IntegerField(blank=True, null=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('full_time', models.BooleanField(blank=True, default=False, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=open_park.models.upload_parking_picture)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
