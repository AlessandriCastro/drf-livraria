# library/swagger_docs.py
from drf_yasg import openapi
from .serializers import AuthorSerializer, BookSerializer

class AuthorSwaggerDocs:
    
    list_docs = {
        'operation_description': "Lista todos os autores com filtro opcional por nome",
        'manual_parameters': [
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY, 
                description="Filtrar autores por nome (busca parcial)", 
                type=openapi.TYPE_STRING,
                required=False
            ),
             openapi.Parameter(
            'aniversario', 
            openapi.IN_QUERY, 
            description="Filtrar autores por data de aniversário", 
            type=openapi.TYPE_STRING,
            required=False
            ),
            openapi.Parameter(
                'email', 
                openapi.IN_QUERY, 
                description="Filtrar autores por email (busca parcial)", 
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'nacionalidade', 
                openapi.IN_QUERY, 
                description="Filtrar autores por nacionalidade (busca parcial)", 
                type=openapi.TYPE_STRING,
                required=False
            )
        ],
        'responses': {
            200: AuthorSerializer(many=True),
            500: "Erro interno do servidor"
        },
        'tags': ['Authors']
    }
    
    create_docs = {
        'operation_description': "Cria um novo autor",
        'request_body': AuthorSerializer,
        'responses': {
            201: AuthorSerializer,
            400: "Dados inválidos - verifique os campos obrigatórios",
            500: "Erro interno do servidor"
        },
        'tags': ['Authors']
    }
    
    retrieve_docs = {
        'operation_description': "Busca um autor específico pelo ID",
        'manual_parameters': [
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID do autor",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        'responses': {
            200: AuthorSerializer,
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem de erro')
                },
                example={'error': 'Autor não encontrado'}
            ),
            500: "Erro interno do servidor"
        },
        'tags': ['Authors']
    }
    
    partial_update_docs = {
        'operation_description': "Atualiza parcialmente um autor existente",
        'manual_parameters': [
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID do autor",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        'request_body': AuthorSerializer,
        'responses': {
            200: AuthorSerializer,
            400: "Dados inválidos",
            404: "Autor não encontrado",
            500: "Erro interno do servidor"
        },
        'tags': ['Authors']
    }
    
    destroy_docs = {
        'operation_description': "Remove um autor do sistema",
        'manual_parameters': [
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID do autor",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        'responses': {
            204: "Autor removido com sucesso",
            404: "Autor não encontrado",
            500: "Erro interno do servidor"
        },
        'tags': ['Authors']
    }
    
    top_5_docs = {
        'operation_description': "Retorna os 5 autores com mais livros publicados",
        'responses': {
            200: AuthorSerializer(many=True),
            500: "Erro interno do servidor"
        },
        'tags': ['Authors']
    }

class BookSwaggerDocs:
    
    list_docs = {
        'operation_description': 'Lista todos os livros com opções de filtro',
        'manual_parameters':[
        openapi.Parameter(
            'titulo',
            openapi.IN_QUERY,
            description='Filtrar por título do livro',
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'ano_publicacao',
            openapi.IN_QUERY,
            description='Filtrar por ano de publicação',
            type=openapi.TYPE_STRING,
            required=False
        ),
         openapi.Parameter(
            'editora',
            openapi.IN_QUERY,
            description='Filtrar por editora',
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'qtd_paginas',
            openapi.IN_QUERY,
            description='Filtrar por quantidade de páginas',
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'isbn',
            openapi.IN_QUERY,
            description='Filtrar por ISBN',
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'idioma',
            openapi.IN_QUERY,
            description='Filtrar por idioma',
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'author',
            openapi.IN_QUERY,
            description='Filtrar por autor',
            type=openapi.TYPE_STRING,
            required=False
        ),
    ],
    'responses':{
        200: "Lista de livros retornada com sucesso"
    },
    'tags':['Books']
    }

    create_docs = {
        'operation_description': "Cria um novo livro",
        'request_body': BookSerializer,
        'responses': {
            201: BookSerializer,
            400: "Dados inválidos",
            500: "Erro interno do servidor"
        },
        'tags': ['Books']
    }

    retrieve_docs = {
        'operation_description': "Busca um livro específico pelo ID",
        'manual_parameters': [
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID do livro",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        'responses': {
            200: BookSerializer,
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem de erro')
                },
                example={'error': 'Livro não encontrado'}
            ),
            500: "Erro interno do servidor"
        },
        'tags': ['Books']
    }
    
    partial_update_docs = {
        'operation_description': "Atualiza parcialmente um livro existente",
        'manual_parameters': [
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID do livro",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        'request_body': BookSerializer,
        'responses': {
            200: BookSerializer,
            400: "Dados inválidos",
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem de erro')
                },
                example={'error': 'livro não encontrado'}
            ),
            500: "Erro interno do servidor"
        },
        'tags': ['Books']
    }
    
    destroy_docs = {
        'operation_description': "Remove um livro do sistema",
        'manual_parameters': [
            openapi.Parameter(
                'pk',
                openapi.IN_PATH,
                description="ID do livro",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        'responses': {
            204: "Livro removido com sucesso",
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem de erro')
                },
                example={'error': 'Livro não encontrado'}
            ),
            500: "Erro interno do servidor"
        },
        'tags': ['Books']
    }
