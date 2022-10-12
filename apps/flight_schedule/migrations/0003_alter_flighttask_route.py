# Generated by Django 4.1.1 on 2022-10-12 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0007_station'),
        ('flight_schedule', '0002_remove_flighttask_aircraft_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flighttask',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_station', to='directory.station'),
        ),
    ]