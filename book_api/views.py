from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import BookSerializer
from .models import Book

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def book(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({'message':'Book deleted successfully!'})
    else:
        return Response(serializer.errors)