# Generated by Django 5.1.4 on 2025-01-07 06:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dealer_id', models.IntegerField()),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Wagon', 'Wagon'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Convertible', 'Convertible')], max_length=20)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2023)])),
                ('horsepower', models.IntegerField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(2000)])),
                ('torque', models.IntegerField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(2000)])),
                ('engine_capacity', models.DecimalField(decimal_places=1, max_digits=4)),
                ('cylinders', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(16)])),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake')),
            ],
        ),
    ]
