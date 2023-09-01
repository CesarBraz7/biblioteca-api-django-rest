from django.db import models

class Biblioteca(models.Model):
    
    # informações do livro
    titulo = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 35)
    preco = models.CharField(max_length = 12)