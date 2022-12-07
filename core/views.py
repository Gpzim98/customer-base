from django.shortcuts import render
from rest_framework import viewsets

from .models import Costumer, Profession
from .serializers import CostumerSerializer, ProfessionSerializer


class CostumerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer