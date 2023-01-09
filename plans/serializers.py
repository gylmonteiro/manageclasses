from rest_framework.serializers import ModelSerializer
from .models import Plan
from sports.serializers import SportSerializer


class PlanSerializer(ModelSerializer):
    sport = SportSerializer(read_only=True)

    class Meta:
        model = Plan
        fields = ("plan", "value_plan", "sport")
