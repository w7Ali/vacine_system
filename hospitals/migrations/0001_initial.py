# Generated by Django 5.0.4 on 2024-05-02 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('contact_number', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hospital_type', models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], max_length=20)),
                ('beds_available', models.IntegerField()),
                ('doctors', models.TextField()),
                ('oxygen_cylinders', models.IntegerField()),
                ('ventilators', models.IntegerField()),
                ('nurses_available', models.IntegerField()),
                ('ambulances', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.city')),
            ],
        ),
    ]
