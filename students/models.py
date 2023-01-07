from django.db import models
from persons.models import Person
from plans.models import Plan

# Create your models here.
class Student(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.SET_NULL, null=True, related_name="student"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    modalitys_arenas = models.ManyToManyField(Plan)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.is_active:
            return f"{self.person.first_name} {self.person.last_name} | Ativo"
        return f"{self.person.first_name} {self.person.last_name} | Inativo"
