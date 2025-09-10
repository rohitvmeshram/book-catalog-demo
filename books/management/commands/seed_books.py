from django.core.management.base import BaseCommand
from django.db import IntegrityError
from books.models import Book

class Command(BaseCommand):
    help = "Seed sample books data into the Book model (idempotent)."

    def handle(self, *args, **options):
        books = [
            {"title": "Sample Book 1", "author": "Sample Author 1", "publication_year": 2023, "isbn": "1112223334444"},
            {"title": "Sample Book 2", "author": "Sample Author 2", "publication_year": 2025, "isbn": "5556667778885"},
            {"title": "Sample Book 3", "author": "Sample Author 3", "publication_year": 2025, "isbn": "9998887776665"},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": 1925, "isbn": "111222333444"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": 1960, "isbn": "555666777888"},
            {"title": "1984", "author": "George Orwell", "publication_year": 1949, "isbn": "999888777666"},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_year": 1813, "isbn": "123456789012"},
            {"title": "The Hobbit", "author": "J.R.R. Tolkien", "publication_year": 1937, "isbn": "987654321598"},
        ]

        created = 0
        for b in books:
            try:
                # Try to get by ISBN (if your model has unique isbn) otherwise adjust key
                obj, was_created = Book.objects.get_or_create(isbn=b.get("isbn"), defaults=b)
                if was_created:
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {obj.title}"))
                else:
                    self.stdout.write(f"Exists: {obj.title}")
            except IntegrityError as e:
                self.stdout.write(self.style.WARNING(f"Integrity error for {b.get('title')}: {e}"))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Skipped {b.get('title')}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"Seeding complete — {created} new books added."))
