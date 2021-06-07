from rest_framework import serializers
from .models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Category
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):

    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date')


class BookDetailSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'categories', 'published_date', 'average_rating',
                  'rating_count', 'thumbnail')


class DatabaseSerializer(serializers.Serializer):
    q = serializers.CharField(required=True)
