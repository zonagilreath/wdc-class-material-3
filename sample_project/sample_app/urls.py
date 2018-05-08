from django.urls import path

from . import views


urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author, name='author_by_id'),
    path('', views.index, name='index'),
]
