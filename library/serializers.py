from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id','nome','aniversario', 'nacionalidade', 'books']
    
    def validate_aniversario(self, value):
        hoje = date.today()
        data_limite = date(hoje.year -18, hoje.month, hoje.day)

        if value > data_limite:
            raise serializers.ValidationError('O autor deve ter pelo menos 18 anos')
        if value < date(1900, 1, 1):
            raise serializers.ValidationError('Data de nascimento muito antiga')
        return value
    


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__'

    def validate_ano_publicacao(self, value):
        if value > 2025:
            raise serializers.ValidationError('Ano não pode ser no futuro')
        return value
    
    def validate_qtd_paginas(self, value):
        if value <=100:
            raise serializers.ValidationError("Livro deve ter pelo menos 100 páginas")
        return value
    
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError('ISBN deve ter 13 dígitos')
        return value
    
    def validate(self, data):
        author = data.get('author')
        ano_publicacao = data.get('ano_publicacao')

        if author and ano_publicacao:
            livros_no_ano = Book.objects.filter(
                author=author,
                ano_publicacao= ano_publicacao
            ).count()

            if self.instance:   
                if (self.instance.author == author and 
                    self.instance.ano_publicacao == ano_publicacao):
                    livros_no_ano -= 1

            if livros_no_ano >= 3:
                raise serializers.ValidationError({
                    'author': f'O autor {author.nome} já publicou {livros_no_ano} em {ano_publicacao}. Limite máximo 3 livros por ano.'
                }) 
        return data


    