from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shelf/<int:shelf_number>/', views.shelf_view, name='shelf'),
    path('shelf/<int:shelf_number>/book/<int:book_id>/', views.book_view, name='book'),
]