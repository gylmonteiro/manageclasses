from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from .models import Class
from students.serializers import StudentSerializer
from teachers.serializers import TeacherSerializer
from sports.serializers import SportSerializer


class ClassSerializer(ModelSerializer):
    student = StudentSerializer()
    teacher = TeacherSerializer()
    sport = SportSerializer()
    # class_all = SerializerMethodField(read_only=True)

    class Meta:
        model = Class
        fields = ("student", "teacher", "sport", "presence", "description")

    # def get_class_all(self, obj):
    #     total = len(list(Class.objects.filter(pk=2)))
    #     aluno = Class.objects.filter(pk=1)

    #     return {"total": total}
