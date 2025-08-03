
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import viewsets
from .models import Author,Book,Category
from .serializers import AuthorSerializer,BookSerializer,CategorySerializer
# Create your views here.

# class BookDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookList(ListCreateAPIView):
    
#     queryset= Book.objects.select_related('category').all()
#     serializer_class= BookSerializer
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields =['title']

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.annotate(book_count=Count('books'))
#     serializer_class = CategorySerializer

# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(book_count=Count('books'))
    serializer_class = CategorySerializer