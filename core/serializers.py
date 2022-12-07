from rest_framework import serializers
from .models import Costumer


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['id', 'name', 'address', 'professions', 'data_sheet']