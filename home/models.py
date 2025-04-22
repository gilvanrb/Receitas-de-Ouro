from django.db import models

class Receitas(models.Model):  
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=150)
    ingredientes = models.TextField()
    preparo = models.TextField()
    imagem = models.ImageField(upload_to='recetas/', null = True, blank=True)
    video_url = models.URLField(null=True, blank=True, help_text="Insira a URL do videdo de preparo (Youtube, etc.)")

    def __str__(self):
        return self.titulo


