from django.urls import path
from .views import BooksAPIView, BooksDetailAPIView, DateBaseAPIView

urlpatterns = [
    path('books/', BooksAPIView.as_view()),
    path('books/<int:id>', BooksDetailAPIView.as_view()),
    path('db/', DateBaseAPIView.as_view()),
]
