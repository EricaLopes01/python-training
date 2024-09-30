from django.db import models

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)             # Campo de texto com comprimento máximo de 100 caracteres
    content = models.TextField()                         # Campo de texto para armazenar o conteúdo do post
    created_at = models.DateTimeField(auto_now_add=True) # Armazena a data e hora de criação do post
    updated_at = models.DateTimeField(auto_now=True)     # Armazena a data e hora de atualização do post
    published = models.BooleanField(default=False)       # Campo booleano indicando se o post está publicado ou não

    def __str__(self):
        return self.title

