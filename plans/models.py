from django.db import models
from sports.models import Sport

# Create your models here.
class Plan(models.Model):
    plans_choices = (
        ("A", "ANUAL"),
        ("T", "TRIMESTRAL"),
        ("M", "MENSAL"),
        ("D", "DIÁRIA"),
        ("S", "SEMESTRAL"),
    )

    plan = models.CharField(max_length=1, choices=plans_choices, blank=True)
    sport = models.ForeignKey(
        Sport, related_name="Plan", on_delete=models.SET_NULL, null=True
    )
    value_plan = models.FloatField()

    def __str__(self) -> str:
        return f"{self.sport} - {self.plan} - R${self.value_plan}"
