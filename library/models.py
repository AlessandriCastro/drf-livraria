from django.db import models


class Author(models.Model):
    nome = models.CharField(max_length= 100)
    aniversario = models.DateField(null=True,blank=True)
    email=models.EmailField(null=True, blank=True)
    bio= models.TextField(null=True, blank= True)
    nacionalidade = models.CharField(max_length=50, null=True,blank=True)
    

    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Book(models.Model):
    titulo = models.CharField(max_length= 100)
    ano_publicacao = models.PositiveIntegerField(max_length=4)
    editora= models.CharField(max_length= 50, null= True, blank= True)
    qtd_paginas= models.IntegerField(null= True, blank = True)
    sinopse = models.TextField(null= True, blank=True)
    isbn = models.CharField(max_length= 13, null=True, blank= True)
    idioma = models.CharField(max_length= 50, null=True, blank= True)

    author = models.ForeignKey(
        Author,
        on_delete= models.CASCADE,
        related_name='books',
    )

    
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo



