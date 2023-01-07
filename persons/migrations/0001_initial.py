# Generated by Django 4.1.5 on 2023-01-07 13:36

import cpf_field.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("addresses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "cpf",
                    cpf_field.models.CPFField(
                        max_length=14,
                        primary_key=True,
                        serialize=False,
                        verbose_name="cpf",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("ddd_number", models.IntegerField(default="84")),
                ("phone_number", models.IntegerField(default="998181036")),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("age", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
                ("photo", models.URLField(blank=True)),
                (
                    "address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="person",
                        to="addresses.address",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="person",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
