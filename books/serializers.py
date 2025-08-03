from rest_framework import serializers
from .models import Book,Author,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','description']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =['title','author','isbn','category','availability_status']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =['name','biography']
