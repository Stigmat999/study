from django import forms

from catalog.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'author', 'publishing_house', 'category', 'year_of_publication']
        model = Book