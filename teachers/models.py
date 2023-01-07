from django.db import models
from persons.models import Person
from sports.models import Sport

# Create your models here.
class Teacher(models.Model):
    person = models.OneToOneField(
        Person, on_delete=models.SET_NULL, null=True, related_name="teacher"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    sport_modalitys = models.ManyToManyField(Sport)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.is_active:
            return f"{self.person.first_name} {self.person.last_name} | Ativo"
        return f"{self.person.first_name} {self.person.last_name} | Inativo"
