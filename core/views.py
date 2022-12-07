from django.shortcuts import render
from rest_framework import viewsets

from .models import Costumer
from .serializers import CostumerSerializer


class CostumerViewSet(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer
