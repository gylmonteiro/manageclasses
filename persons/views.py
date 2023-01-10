from rest_framework.viewsets import ModelViewSet
from .models import Person
from .serializers import PersonSerializer

# Create your views here.
class PersonViewSet(ModelViewSet):
    queryset = Person.objects.filter(is_active = True)
    serializer_class = PersonSerializer

