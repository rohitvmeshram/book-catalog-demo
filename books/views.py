from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
import requests
from django.conf import settings
from django.shortcuts import render
from django.db.models import Count

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FetchBookView(APIView):
    def get(self, request):
        isbn = request.query_params.get('isbn')
        if not isbn:
            return Response({"error": "ISBN is required"}, status=400)
        
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={settings.GOOGLE_BOOKS_API_KEY}"
        response = requests.get(url)
        
        if response.status_code != 200:
            return Response({"error": "Failed to fetch book data"}, status=response.status_code)
        
        data = response.json()
        if not data.get('items'):
            return Response({"error": "Book not found"}, status=404)
        
        book_data = data['items'][0]['volumeInfo']
        book = {
            'title': book_data.get('title', 'Unknown'),
            'author': ', '.join(book_data.get('authors', ['Unknown'])),
            'publication_year': int(book_data.get('publishedDate', '2000')[:4]),
            'isbn': isbn
        }
        
        serializer = BookSerializer(data=book)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def visualization_view(request):
    data = Book.objects.values('publication_year').annotate(count=Count('id')).order_by('publication_year')
    years = [item['publication_year'] for item in data]
    counts = [item['count'] for item in data]
    return render(request, 'visualization.html', {'years': years, 'counts': counts})