from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import HttpResponseForbidden, HttpResponseNotAllowed

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

    def list(self, request, *args, **kwargs):
        custumers = Custumer.objects.all()
        serializer = CustumerSerializer(custumers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('Not Allowed')

    def create(self, request, *args, **kwargs):
        data = request.data
        custumer = Custumer.objects.create(
            name=data['name'], address=data['address'], data_sheet_id=data['data_sheet']
        )
        profession = Profession.objects.get(id=data['profession'])

        for p in custumer.professions.all():
            custumer.professions.remove(p)
        custumer.professions.add(profession)
        custumer.save()

        serializer = CustumerSerializer(custumer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        custumer = self.get_object()
        data = request.data
        custumer.name = data['name']
        custumer.address = data['address']
        custumer.data_sheet_id = data['data_sheet']

        profession = Profession.objects.get(id=data['profession'])

        custumer.professions.add(profession)
        custumer.save()

        serializer = CustumerSerializer(custumer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        custumer = self.get_object()
        custumer.name = request.data.get('name', custumer.name)
        custumer.address = request.data.get('address', custumer.address)
        custumer.data_sheet_id = request.data.get('data_sheet', custumer.data_sheet_id)

        custumer.save()
        serializer = CustumerSerializer(custumer)
        return Response(serializer.data)


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
