from rest_framework.serializers import ModelSerializer
from .models import Student
from persons.serializers import PersonSerializer


class StudentSerializer(ModelSerializer):
    person = PersonSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ("person", "is_active")
