from django.db import models

# criacao da model

class TreinadorModel(models.Model):
    nome = models.CharField(max_length=255)
    qtd_treinadores = models.IntegerField()
    descricao_treinadores = models.TextField()
    personagens = models.CharField(max_length=255)

    def __str__(self):
        return f'o treinador {self.nome} foi criado'


class PokemonModel(models.Model):
    nome = models.CharField(max_length=255)
    qtd_pokemons = models.IntegerField()
    descricao_pokemons = models.TextField()
    personagens = models.CharField(max_length=255)
    treinador = models.ForeignKey(TreinadorModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'o pokemon {self.nome} foi criado'