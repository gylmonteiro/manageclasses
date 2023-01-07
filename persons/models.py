from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.models import User
from addresses.models import Address

# Create your models here.


class Person(models.Model):
    user = models.ForeignKey(
        User, related_name="person", on_delete=models.CASCADE, null=True
    )
    cpf = CPFField("cpf", primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    ddd_number = models.IntegerField(default="84")
    phone_number = models.IntegerField(default="998181036")
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
    is_active = models.BooleanField(default=False)
    photo = models.URLField(blank=True)
    address = models.ForeignKey(
        Address, related_name="person", on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return f"{self.first_name.upper()} {self.last_name.upper()} | CPF {self.cpf}"
