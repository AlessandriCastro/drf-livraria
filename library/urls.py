from django.urls import path
from .views import AuthorViewSet, BookViewSet

author_list = AuthorViewSet.as_view({'get':'list', 'post': 'create'})
author_detail = AuthorViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})

author_top_5 = AuthorViewSet.as_view({'get': 'list_5_autores'})

book_list = BookViewSet.as_view({'get':'list', 'post':'create'})
book_detail = BookViewSet.as_view({'get':'retrieve', 'patch': 'partial_update', 'delete':'destroy'})

urlpatterns = [
    path('authors/', author_list, name ='author-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
    path('authors/top-5/', author_top_5, name='author-top-5'),

    path('books/',book_list, name ='book-list'),
    path('books/<int:pk>/', book_detail, name= 'book-detail'),
]