from rest_framework.serializers import ModelSerializer
from .models import Sport


class SportSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = ["name"]
