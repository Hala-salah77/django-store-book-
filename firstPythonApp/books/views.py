import imp
from multiprocessing import context
from django.shortcuts import render ,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Author,Book
# Create your views here.



def index(request):
    return HttpResponse("hello")

def all_books(request):
    context={
        "books":Book.objects.all()
    }
    return render(request,"books/books.html",context=context)


def show_book(request,id):
    book=get_object_or_404(Book,id=id)
    context={
        "book":book
    }
    return render(request,"books/book_details.html",context=context)


def show_book_author(request,id):
    author=get_object_or_404(Author,id=id)
    book_author=Book.objects.filter(author_id=id)
    print(book_author)
    context={
        "book_author":book_author,
        "author":author
    }
    return render(request,"books/book_author.html",context=context)
