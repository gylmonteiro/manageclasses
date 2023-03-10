# Generated by Django 4.1.5 on 2023-01-07 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("students", "0001_initial"),
        ("activities", "0001_initial"),
        ("sports", "0001_initial"),
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True)),
                (
                    "activity",
                    models.ManyToManyField(
                        related_name="classes", to="activities.activity"
                    ),
                ),
                (
                    "sport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classes",
                        to="sports.sport",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classes",
                        to="students.student",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classes",
                        to="teachers.teacher",
                    ),
                ),
            ],
        ),
    ]
