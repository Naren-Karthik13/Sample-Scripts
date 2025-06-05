from django.shortcuts import render
from .models import Collection, Item
# Create your views here.

def index(request):
    collection = Collection.objects.all()
    return render(request, 'index.html', {'collection': collection})

def category(request,category):
     collection = Collection.objects.get(category=category) 
     item = Item.objects.filter(collection=collection)
     context = {
         'collection': collection,
         'item': item
     }
     return render(request, 'category.html', context)
 