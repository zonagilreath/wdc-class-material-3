from django.urls import path

from . import views


urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author, name='author_by_id'),
    path('create_book', views.create_book, name='create_book'),
    path('', views.index, name='index'),
]
