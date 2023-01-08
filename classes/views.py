from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Class
from .serializers import ClassSerializer


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()

    print(len(list(queryset)))
    serializer_class = ClassSerializer
