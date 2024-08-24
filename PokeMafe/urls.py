from django.urls import path, include
from .viewsets import PokemonViewSet, TreinadorViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r"Pokemons", PokemonViewSet)
router.register(r"Treinadores", TreinadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('PokemonViewSet', PokemonViewSet.as_view({'get': 'list'})),
    path('TreinadorViewSet', TreinadorViewSet.as_view({'get': 'list'}))
]