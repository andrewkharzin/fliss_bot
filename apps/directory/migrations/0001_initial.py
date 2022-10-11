# Generated by Django 4.1.1 on 2022-10-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "iata",
                    models.CharField(default="", max_length=2, verbose_name="Iata"),
                ),
                (
                    "icao",
                    models.CharField(default="", max_length=3, verbose_name="Icao"),
                ),
                (
                    "rus_code",
                    models.CharField(default="", max_length=2, verbose_name="Rus"),
                ),
                (
                    "comment_eng",
                    models.CharField(
                        default="", max_length=85, verbose_name="Description eng"
                    ),
                ),
                (
                    "comment_rus",
                    models.CharField(
                        default="", max_length=85, verbose_name="Description rus"
                    ),
                ),
                (
                    "country",
                    models.CharField(default="", max_length=85, verbose_name="Country"),
                ),
                (
                    "alliance",
                    models.CharField(default="", max_length=5, verbose_name="Alliance"),
                ),
                (
                    "lowcost",
                    models.CharField(default="", max_length=1, verbose_name="Lowcost"),
                ),
                (
                    "description",
                    models.CharField(
                        default="", max_length=50, verbose_name="Description"
                    ),
                ),
            ],
        ),
    ]