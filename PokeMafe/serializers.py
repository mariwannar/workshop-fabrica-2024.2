from rest_framework import serializers
from .models import PokemonModel, TreinadorModel

# criacao do serializer da model pokemon XD

class PokemonSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PokemonModel
        fields = ('__all__')

class TreinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreinadorModel
        fields = ('__all__')