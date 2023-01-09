from rest_framework.viewsets import ModelViewSet
from .serializers import SportSerializer
from .models import Sport


class SportViewSet(ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
