import json
from django.core.management.base import BaseCommand

import urllib.request


from books_rest.books.models import Author, Category, Book


class CommandBased(BaseCommand):

    def handle(self, *args, **options):
        with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=Hobbit") as url:
            data = json.loads(url.read().decode())
            print(data)
            empty = {}
            for book_item in data['items']:
                empty['title'] = book_item['volumeInfo'].get('title')
                empty['published_date'] = int(book_item['volumeInfo'].get('publishedDate')[:4])
                empty['rating_count'] = book_item['volumeInfo'].get('ratingsCount', None)
                empty['average_rating'] = book_item['volumeInfo'].get('averageRating', None)
                empty['thumbnail'] = book_item['volumeInfo']['imageLinks'].get('thumbnail')
                book, created = Book.objects.get_or_create(**empty)
                list_category = book_item['volumeInfo'].get('categories')
                list_author = book_item['volumeInfo'].get('authors')

                for name in list_author:
                    name = name.strip()
                    author, created = Author.objects.get_or_create(name=name)
                    book.authors.add(author)

                if list_category:
                    for name in list_category:
                        name = name.strip()
                        category, created = Category.objects.get_or_create(name=name)
                        book.categories.add(category)
                book.save()
                print(book)


