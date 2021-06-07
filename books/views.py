from django.shortcuts import render, HttpResponse
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
from rest_framework.filters import OrderingFilter, SearchFilter

import json
import urllib.request

from .models import Book, Category, Author
from .serializers import BookSerializer, DatabaseSerializer, BookDetailSerializer


class BooksAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter, SearchFilter]
    lookup_field = 'id'
    filterset_fields = ['published_date']
    filterset_fields = ['authors']
    ordering_fields = ['published_date']
    search_fields = ['authors__name']


class BooksDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        book = self.get_object(id)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)


class DateBaseAPIView(APIView):

    def post(self, request):
        serializer = DatabaseSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        query = serializer.data["q"]

        with urllib.request.urlopen(f"https://www.googleapis.com/books/v1/volumes?q={query}") as url:
            data = json.loads(url.read().decode())
        return Response(data)


