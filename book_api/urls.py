from django.urls import path
from .views import book_list, book_create, book

urlpatterns = [
    path('books/', book_list, name="book_list" ),
    path('books/create/', book_create, name='book_create'),
    path('books/<int:pk>/', book, name='book_detail')
]