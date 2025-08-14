from django.shortcuts import render
from rest_framework import viewsets
from .models import Borrow
from .serializers import BorrowSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes=[IsAuthenticated]
    

