from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='books')
    availability_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
