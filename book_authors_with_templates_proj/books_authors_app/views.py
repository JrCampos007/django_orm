from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])

    return redirect('/')

def book_detail(request, id):
    if request.method == "POST":
        context = {
            "book": Book.objects.get(id=request.POST['book_id']),
            "authors": Author.objects.exclude(books=Book.objects.get(id=request.POST['book_id'])),
        }

    return render(request, 'books.html', context)

def assign_author(request):
    if request.method == "POST":
        book = Book.objects.get(id=request.POST['book_id'])             # many-to-many requires instantiate both and then add
        author = Author.objects.get(id=request.POST['new_author'])
        book.authors.add(author)
    
    return redirect('/authors')     # a redirect requires the /slash! 

def authors(request):
    context = {
        "all_authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)


def add_author(request): 
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], notes=request.POST['notes'])

    return redirect('/')

def author_detail(request, id):
    if request.method == "POST":
        context = {
            "author": Author.objects.get(id=request.POST['author_id']),
            "books": Book.objects.exclude(authors=Author.objects.get(id=request.POST['author_id'])),
        }

    return render(request, 'author_detail.html', context)

def assign_book(request):
    if request.method == "POST":
        book = Book.objects.get(id=request.POST['new_book'])             # many-to-many requires instantiate both and then add
        author = Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    
    return redirect('/authors')     # a redirect requires the /slash! 

# Create your views here.
