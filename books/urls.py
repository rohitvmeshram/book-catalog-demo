from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView, FetchBookView, visualization_view

urlpatterns = [
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
    path('api/fetch-book/', FetchBookView.as_view(), name='fetch-book'),
    path('visualization/', visualization_view, name='visualization'),
]