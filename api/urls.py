from django.urls import path,include
from rest_framework import routers
from rest_framework_nested import routers
from books.views import AuthorViewSet,BookViewSet,CategoryViewSet
from borrow.views import BorrowViewSet
from members.views import MemberViewSet
router = routers.DefaultRouter()
router.register('books',BookViewSet,basename='books')
router.register('categories',CategoryViewSet)
router.register('author',AuthorViewSet,basename='book-author')
router.register('borrow',BorrowViewSet)
router.register('member',MemberViewSet)

book_router = routers.NestedDefaultRouter(router,'books',lookup='book')
book_router.register('authors',AuthorViewSet,basename='book-authors')

borrow_router = routers.NestedDefaultRouter(router,'borrow',lookup='borrow')
borrow_router.register('members',MemberViewSet,basename='borrow-member')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(book_router.urls)),
    path('',include(borrow_router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),

]
