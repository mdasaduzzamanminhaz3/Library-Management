
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import Author,Book,Category
from .serializers import AuthorSerializer,BookSerializer,CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import  IsLibrarian,IsMemberOrReadOnly
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

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAuthenticated(),IsLibrarian()]
        return [IsAuthenticated(),IsMemberOrReadOnly()]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAuthenticated(),IsLibrarian()]
        return [IsAuthenticated()]
# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.annotate(book_count=Count('books'))
#     serializer_class = CategorySerializer

# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(book_count=Count('books'))
    serializer_class = CategorySerializer
    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            return [IsAuthenticated(),IsLibrarian()]
        return [IsAuthenticated()]