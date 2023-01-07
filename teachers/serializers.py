from rest_framework.serializers import ModelSerializer
from .models import Teacher
from persons.serializers import PersonSerializer


class TeacherSerializer(ModelSerializer):
    person = PersonSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ("person", "is_active")
