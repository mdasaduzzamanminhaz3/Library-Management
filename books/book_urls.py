from django.urls import path
from books import views

urlpatterns =[
    path('<int:pk>/',views.BookDetails.as_view(),name='book'),
    path('',views.BookList.as_view(),name='book-list'),
    path('',views.AuthorViewSet.as_view(),name='author')
]