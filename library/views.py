from rest_framework import viewsets
from .models import Author,Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ViewSet):
    queryset = Author.objects.all()
    serializer_class= AuthorSerializer

    

class BookViewSet(viewsets.ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

