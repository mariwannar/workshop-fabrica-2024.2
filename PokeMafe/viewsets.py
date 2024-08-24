from rest_framework import viewsets
from .models import PokemonModel, TreinadorModel
from .serializers import PokemonSerializer, TreinadorSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = PokemonModel.objects.all()
    serializer_class = PokemonSerializer

class TreinadorViewSet(viewsets.ModelViewSet):
    queryset = TreinadorModel.objects.all()
    serializer_class = TreinadorSerializer