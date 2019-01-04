from django.shortcuts import render
from rest_framework import viewsets
from .models import Operacao, Upload
from .serializers import OperacaoSerializer, UploadSerializer
from rest_framework import routers


class OperacaoViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    
