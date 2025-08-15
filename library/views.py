from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Author,Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Author.objects.all()
        if 'nome' in request.GET:
            queryset = queryset.filter(nome__icontains=request.GET['nome'])

        if 'nome' in request.GET:
            queryset = queryset.filter(nome__icontains=request.GET['nome'])

        serializer = AuthorSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def list_5_autores(self, request):
        queryset = Author.objects.all()

        for q in queryset:
            Book.objects.filter(author=q).count()

        serializer = AuthorSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer= AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    def update(self,request, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response(
                {'error': 'Autor não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
    def partial_update(self, resquest, pk):
        try:
            author = Author.objects.get(pk=pk)
            serializer = AuthorSerializer(author, data= resquest.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response(
                {'error':'Autor não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )
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
    queryset = Book.objects.all()
    serializer_class = BookSerializer

