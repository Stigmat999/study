from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    year_of_birth = models.IntegerField(null=True)
    hometown = models.CharField(max_length=50, null=True)
    basic_genre = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    year_of_foundation = models.IntegerField(null=True)
    short_description = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=100, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    popularity = models.CharField(max_length=10, null=True)
    number_of_books = models.IntegerField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    publishing_house = models.ForeignKey(PublishingHouse)
    category = models.ForeignKey(Category)
    year_of_publication = models.IntegerField(null=True)
