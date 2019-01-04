from rest_framework import serializers
from .models import Operacao, Upload

class OperacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operacao
        fields = ('id', 'titulo', 'duracao', 'nome_arquivo','video')

class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = ('id', 'startime', 'endtime', 'nome','file') 

        
