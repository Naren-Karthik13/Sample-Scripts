from django.shortcuts import render,get_object_or_404
from .models import Book
from .models import Shelf

# Create your views here.
context = {
    'books': Book.objects.all(),
    'shelves': Shelf.objects.all(),
}
def home(request):
    return render(request, 'home.html', context)

def shelf_view(request,shelf_number):
    shelf = Shelf.objects.get(shelf_number=shelf_number)
    books = shelf.book_set.all()
    context = {
    'shelves': shelf,
    'books': books,
    }
    return render(request, 'shelf.html', context)

def book_view(request, book_id,**kwargs):
    book = get_object_or_404(Book, id=book_id)
    shelf = book.shelf
    context = {
        'book': book,
        'shelf': shelf,
    }
    return render(request, 'book.html', context)