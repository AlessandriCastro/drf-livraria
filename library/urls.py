from django.urls import path
from .views import AuthorViewSet, BookViewSet

author_list = AuthorViewSet.as_view({'get':'list', 'post': 'create'})
author_detail = AuthorViewSet.as_view({'get': 'retrieve', 'put':'update', 'patch': 'partial_update', 'delete': 'destroy'})

book_list = BookViewSet.as_view({'get':'list', 'post':'create'})
book_detail = BookViewSet.as_view({'get':'retrieve', 'put':'update', 'patch': 'partial_update', 'delete':'destroy'})

urlpatterns = [
    path('authors/', author_list, name ='author-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
    path('books/',book_list, name ='book-list'),
    path('books/<int:pk>/', book_detail, name= 'book-detail'),
]