from django.urls import path
from .views import book_list, book_create, book

urlpatterns = [
    path('list/', book_list, name="book_list" ),
    path('list/create/', book_create, name='book_create'),
    path('list/<int:pk>/', book, name='book_detail')
]