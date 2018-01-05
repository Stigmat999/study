from rest_framework.serializers import ModelSerializer
from catalog.models import Author, PublishingHouse, Category, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class PublishingHouseSerializer(ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = ('name',)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    publishing_house = PublishingHouseSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ('title', 'author', 'publishing_house', 'category', 'year_of_publication')
