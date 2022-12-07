from rest_framework import serializers
from .models import Costumer, Profession


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['id', 'name', 'address', 'professions', 'data_sheet']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description']