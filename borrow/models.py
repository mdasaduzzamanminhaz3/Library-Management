from django.db import models
from books.models import Book
from members.models import Member
# Create your models here.
class Borrow(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True,blank=True)