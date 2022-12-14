from rest_framework import serializers
from .models import (
    Custumer,
    Profession,
    Document,
    DataSheet
)


class CustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custumer
        fields = ['id', 'name', 'address', 'professions', 'data_sheet', 'active']


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'description']


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ['id', 'description', 'historical_data']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'dtype', 'doc_number', 'custumer']