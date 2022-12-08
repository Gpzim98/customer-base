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
    queryset = Custumer.objects.all()
    serializer_class = CustumerSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
