from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from .models import Author,Book
from .serializers import AuthorSerializer, BookSerializer
from .swagger import AuthorSwaggerDocs, BookSwaggerDocs
from .telegram_bot import notificar_autor_criado

class AuthorViewSet(viewsets.ViewSet):
    @swagger_auto_schema(**AuthorSwaggerDocs.list_docs)        
    def list(self, request):
        queryset = Author.objects.all()
        if 'nome' in request.GET:
            queryset = queryset.filter(nome__icontains=request.GET['nome'])

        if 'aniversario' in request.GET:
            queryset = queryset.filter(aniversario__icontains=request.GET['aniversario'])
        
        if 'email' in request.GET:
            queryset = queryset.filter(email__icontains=request.GET['email'])

        if 'nacionalidade' in request.GET:
            queryset = queryset.filter(nacionalidade__icontains=request.GET['nacionalidade'])

        serializer = AuthorSerializer(queryset, many = True)
        return Response(serializer.data)
    
    @swagger_auto_schema(**AuthorSwaggerDocs.top_5_docs)
    @action(detail=False, methods=['get'], url_path='top-5')
    def list_5_autores(self, request):
        autores = Author.objects.all()
        autores_com_contagem = []

        for autor in autores:
            book_count = Book.objects.filter(author=autor).count()
            autores_com_contagem.append({
            'autor': autor,
            'quantidade_livros': book_count
        })
    
        autores_com_contagem.sort(key=lambda x: x['quantidade_livros'], reverse=True)
        
       
        top_5_autores = autores_com_contagem[:5]
        
        top_5_apenas_autores = [item['autor'] for item in top_5_autores]
        
        serializer = AuthorSerializer(top_5_apenas_autores, many = True)
        return Response(serializer.data)


    @swagger_auto_schema(**AuthorSwaggerDocs.create_docs)
    def create(self,request):
        serializer= AuthorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            autor=serializer.save()

            print("🎯 TENTANDO ENVIAR NOTIFICAÇÃO...")
            try:
                notificar_autor_criado(autor)
            except Exception as e:
                print(f"❌ ERRO NA NOTIFICAÇÃO: {e}")

                notificar_autor_criado(autor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    

    @swagger_auto_schema(**AuthorSwaggerDocs.retrieve_docs)
    def retrieve(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response(
                {'error': 'Autor não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        

    @swagger_auto_schema(**AuthorSwaggerDocs.partial_update_docs)
    def partial_update(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author, data= request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
        except Author.DoesNotExist:
            return Response(
                {'error':'Autor não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        

    @swagger_auto_schema(**AuthorSwaggerDocs.destroy_docs)
    def destroy(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response(
                {'error': 'Autor não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
    

class BookViewSet(viewsets.ViewSet):
    @swagger_auto_schema(**BookSwaggerDocs.list_docs)
    def list(self, request):
        queryset=Book.objects.all()
        if 'titulo' in request.GET:
            queryset = queryset.filter(nome__icontains=request.GET['titulo'])

        if 'ano_publicacao' in request.GET:
            queryset = queryset.filter(ano_publicacao__icontains=request.GET['ano_publicacao'])
        
        if 'editora' in request.GET:
            queryset = queryset.filter(editora__icontains=request.GET['editora'])

        if 'qtd_paginas' in request.GET:
            queryset= queryset.filter(qtd_paginas__icontains=request.GET['qtd_paginas'])

        if 'isbn' in request.GET:
            queryset = queryset.filter(isbn__icontains=request.GET['isbn'])

        if 'idioma' in request.GET:
            queryset= queryset.filter(idioma__icontains=request.GET['idioma'])

        if 'author' in request.GET:
            queryset= queryset.filter(author__nome__icontains=request.GET['author'])

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(**BookSwaggerDocs.create_docs)
    def create(self,request):
        serializer= BookSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
    @swagger_auto_schema(**BookSwaggerDocs.retrieve_docs)
    def retrieve(self, request, pk):
        try:
            book= Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(
                {'error': 'Livro não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(**BookSwaggerDocs.partial_update_docs)
    def partial_update(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data= request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
        except Book.DoesNotExist:
            return Response(
                {'error':'livro não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
        
    @swagger_auto_schema(**BookSwaggerDocs.destroy_docs)
    def destroy(self,request,pk):
        try: 
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(
                {'error':'Livro não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )