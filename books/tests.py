from django.test import TestCase
from rest_framework.test import APIClient
from .models import Book
import uuid  # Add this for generating unique ISBNs

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_year': 2023,
            'isbn': '1234567890123'
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        new_book_data = {
            'title': 'New Test Book',
            'author': 'New Author',
            'publication_year': 2024,
            'isbn': str(uuid.uuid4())[:13]  # Generate a unique 13-char ISBN
        }
        response = self.client.post('/api/books/', new_book_data, format='json')
        print(response.data)  # Debug output to see the response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)  # Check total books

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_update_book(self):
        updated_data = self.book_data.copy()
        updated_data['title'] = 'Updated Title'
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 204)