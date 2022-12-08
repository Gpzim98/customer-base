from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Custumer,
    Profession,
    DataSheet, Document
)

from .serializers import (
    CustumerSerializer,
    ProfessionSerializer,
    DataSheetSerializer,
    DocumentSerializer,

)


class CustumerViewSet(viewsets.ModelViewSet):
    serializer_class = CustumerSerializer

    def get_queryset(self):
        active_custumers = Custumer.objects.filter(active=True)
        return active_custumers


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
