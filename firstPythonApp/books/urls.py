from django.urls import path
from .views import index , all_books , show_book ,show_book_author


urlpatterns = [
    path('', all_books ,name='index'),
    path('book/<int:id>',show_book),
    path('author/<int:id>',show_book_author)
]
