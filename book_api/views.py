from django.shortcuts import render
from django.http import JsonResponse
from .serializer import BookSerializer
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    