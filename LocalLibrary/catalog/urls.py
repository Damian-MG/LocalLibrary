from django.urls import re_path as url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # Challenge yourself (3)
	path('authors/', views.AuthorListView.as_view(), name="authors"),
	path('author/<int:pk>/', views.AuthorDetailView.as_view(), name="author-detail"),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allborrowedbooks/', views.AllLoanedBooksListView.as_view(), name='all-borrowed'),
]