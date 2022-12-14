# Generated by Django 4.1.1 on 2022-10-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("directory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Register",
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
                    "number",
                    models.CharField(default="", max_length=5, verbose_name="Number"),
                ),
                (
                    "ac_type",
                    models.CharField(default="", max_length=3, verbose_name="Type"),
                ),
                ("co", models.CharField(default="", max_length=5, verbose_name="@Co")),
                (
                    "mod",
                    models.CharField(
                        default="", max_length=4, verbose_name="Modification"
                    ),
                ),
                (
                    "g_type",
                    models.CharField(default="", max_length=5, verbose_name="G_TYPE"),
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
