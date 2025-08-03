from django.urls import path
from books import views

urlpatterns = [
    path('',views.CategoryList.as_view(),name='category-list'),
    path('',views.CategoryDetails.as_view(),name='view-specific-category')
]