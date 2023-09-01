from rest_framework import serializers
from .models import Biblioteca

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        #serializar as models de python para json
        model = Biblioteca 
        fields = '__all__'