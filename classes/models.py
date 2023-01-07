from django.db import models
from students.models import Student
from teachers.models import Teacher
from sports.models import Sport
from activities.models import Activity


# Create your models here.
class Class(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="classes"
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="classes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="classes")
    activity = models.ManyToManyField(Activity, related_name="classes")
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.student} | {self.sport} | {self.created_at.strftime('%d/%m/%Y')}"
