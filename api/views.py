from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.serializers import UdyamSerializer
from api.models import UdyamForm


class UdyamViewSet(viewsets.ModelViewSet):
   queryset = UdyamForm.objects.all()
   serializer_class = UdyamSerializer