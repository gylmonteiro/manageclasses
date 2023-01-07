from rest_framework.serializers import ModelSerializer
from .models import Class
from students.serializers import StudentSerializer
from teachers.serializers import TeacherSerializer
from sports.serializers import SportSerializer


class ClassSerializer(ModelSerializer):
    student = StudentSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    sport = SportSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ("student", "teacher", "sport", "presence", "description")
