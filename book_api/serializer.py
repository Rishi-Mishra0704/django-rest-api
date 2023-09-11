from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price')

    def create(self, data):
        return Book.objects.create(**data)
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.author = data.get('author', instance.author)
        instance.price = data.get('price', instance.price)
        instance.save()
        return instance
