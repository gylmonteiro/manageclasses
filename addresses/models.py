from django.db import models

# Create your models here.
class Address(models.Model):
    postal_code = models.CharField(max_length=8, default="59650-000")
    street = models.TextField(blank=True)
    district = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.district} | {self.postal_code}"
