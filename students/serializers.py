from rest_framework.serializers import ModelSerializer
from .models import Student
from persons.serializers import PersonSerializer


class StudentSerializer(ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Student
        fields = "__all__"
