# Generated by Django 4.1.1 on 2022-10-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_schedule', '0004_remove_flighttask_is_return_alter_flighttask_payload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flighttask',
            name='payload',
            field=models.CharField(default='', max_length=50, verbose_name='Payload(kg)'),
        ),
    ]
