from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, this is the home page of the new project!")

def about_page_view(request):  # new
    return render(request, "pages/about.html")