from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime

from .models import Author, Book


def index(request):
    sort_method = request.GET.get('sort', 'asc')
    books = Book.objects.all()
    if sort_method == 'asc':
        books = books.order_by('popularity')
    elif sort_method == 'desc':
        books = books.order_by('-popularity')
    return render(request, 'index.html', {
        'books': books,
        'sort_method': sort_method
    })


def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {
        'authors': authors
    })


def author(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return HttpResponseNotFound()

    return render(request, 'author.html', {
        'author': author
    })
