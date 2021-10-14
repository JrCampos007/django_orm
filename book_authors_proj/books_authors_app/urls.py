from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:id>', views.book_detail),
    path('assign_author', views.assign_author),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:id>', views.author_detail),
    path('assign_book', views.assign_book),
]