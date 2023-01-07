
from django.db import models

# Create your models here.
class Activity (models.Model):

    level_choiches = (
        ("I", "INICIANTE"),
        ("M", "MÉDIO"),
        ("A", "AVANÇADO")
    )

    name_activity = models.CharField(max_length=250)
    level = models.CharField(max_length=1, choices=level_choiches)

    def __str__(self) -> str:
        return (f"{self.name_activity} -> {self.level}")