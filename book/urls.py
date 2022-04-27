from django.urls import path
from . import views

add_name ='book'

urlpatterns = [
    path('hello/', views.hello_word, name='hello'),
    path('book/', views.book_all, name='book_all'),
    path('book/latest/', views.book_latest, name='book_latest'),
    path('book/detective/', views.book_genre_detective, name='book_detective'),
    path('book/romace/', views.book_genre_romace, name='book_romace'),
    path('book/fantasies/', views.book_genre_fantasies, name='book_fantasies'),
    path('book/anime/', views.book_genre_anime, name='book_anime'),
    path('book/<int:id>/', views.books_detail, name='books_detail'),
    path('book/<int:id>/update/', views.put_update_book, name='books_update'),
    path('book/<int:id>/delete/', views.book_delete, name='books_delete'),
    path('add-book/', views.add_book, name='add_book')

]
