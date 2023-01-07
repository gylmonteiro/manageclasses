# Generated by Django 4.1.5 on 2023-01-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                ("name_activity", models.CharField(max_length=250)),
                (
                    "level",
                    models.CharField(
                        choices=[("I", "INICIANTE"), ("M", "MÉDIO"), ("A", "AVANÇADO")],
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]