from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    published_date = models.IntegerField()
    average_rating = models.FloatField(null=True)
    rating_count = models.IntegerField(null=True)
    thumbnail = models.URLField(max_length=150)

    def __str__(self):
        return self.title

