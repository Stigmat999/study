# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from catalog.forms import BookForm
from catalog.models import Book
from catalog.serializers import BookSerializer


def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookForm()
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books, 'form': form})


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
