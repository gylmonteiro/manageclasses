# Generated by Django 4.1.5 on 2023-01-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="presence",
            field=models.BooleanField(default=True),
        ),
    ]