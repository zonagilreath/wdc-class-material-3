from datetime import datetime

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Author, Book

import re


def index(request):
    sort_method = request.GET.get('sort', 'asc')
    books = Book.objects.all()
    if sort_method == 'asc':
        books = books.order_by('popularity')
    elif sort_method == 'desc':
        books = books.order_by('-popularity')
        
    context = {
        'books': books,
        'authors': Author.objects.all(),
        'sort_method': sort_method,
    }
    
    return render(request, 'index.html', context)


def create_book(request):
    book_data = {
        'title': request.POST['title'],
        'author': request.POST['author'],
        'isbn': request.POST['isbn'],
        'popularity': request.POST['popularity'],
    }
    
    
    '''
    ISBN-10 and -13 basic form validator
    doesn't validate check-digit
    '''
    def is_isbn(isbn):
        isbn = isbn.replace("-", "").replace(" ", "").upper()
        match_10 = re.search(r'^(\d{9})(\d|X)$', isbn)
        match_13 = re.search(r'^(\d{12})(\d|X)$', isbn)
        return (match_10 or match_13)
    
    if len(book_data['title'].strip()) == 0:
        messages.add_message(request, messages.ERROR, 'Please enter a title')
    if not is_isbn(book_data['isbn']):
        print('second if passing')
        messages.add_message(request, messages.ERROR, 'Please enter a valid ISBN 10 or ISBN 13')
    
    if messages.get_messages(request):
        return redirect('index')
    
    messages.success(request, 'Book has been created!')
    
    author = get_object_or_404(Author, id=book_data['author'])
    
    new_book = Book.objects.create(
        title = book_data['title'],
        author = author,
        isbn = book_data['isbn'],
        popularity = book_data['popularity']
        )
    
    return render(request, 'create_book.html', {
        'data': book_data
    })
    
    
def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {
        'authors': authors
    })


def author(request, author_id):
        
    author = get_object_or_404(Author, id=author_id)

    return render(request, 'author.html', {
        'author': author
    })
