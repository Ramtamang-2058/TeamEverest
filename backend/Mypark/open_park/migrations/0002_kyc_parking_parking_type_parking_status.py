# Generated by Django 4.2.5 on 2023-09-15 16:53

from django.db import migrations, models
import open_park.models


class Migration(migrations.Migration):

    dependencies = [
        ('open_park', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_code', models.CharField(blank=True, max_length=255, null=True)),
                ('citizenship_id', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=open_park.models.upload_kyc_picture)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='parking',
            name='parking_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='parking',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
