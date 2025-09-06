# Book Catalog Web Application

This is a Django-based web application for managing a book catalog with CRUD functionality, integrated with the Google Books API, and featuring an enhanced data visualization. The application uses PostgreSQL as the database (local or Supabase).

## Features
- **CRUD Operations**: Manage books (Create, Read, Update, Delete) via REST APIs.
- **Third-Party API Integration**: Fetch book details from the Google Books API using ISBN.
- **Data Visualization**: Display an attractive bar chart of books grouped by publication year with gradients, tooltips, and responsive design.

## Prerequisites
- Python 3.12+
- PostgreSQL (or Supabase account)
- Git
- Google Books API Key (from Google Cloud Console)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/book-catalog-demo.git
   cd book-catalog-demo
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**
   - Create a database named `book_catalog` and user with privileges.
   - Update `book_catalog/settings.py` with your credentials.

5. **Set Up Environment Variables**
   - Create `.env`:
     ```env
     GOOGLE_BOOKS_API_KEY=your_api_key
     ```

6. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   - Access at `http://127.0.0.1:8000/` (redirects to visualization).

## API Endpoints
- **List/Create Books**: `GET/POST /api/books/`
- **Retrieve/Update/Delete Book**: `GET/PUT/DELETE /api/books/<id>/`
- **Fetch from Google Books**: `GET /api/fetch-book/?isbn=<isbn>`
- **Visualization**: `GET /visualization/`

## Testing
- Run tests: `python manage.py test`

## Adding Test Data
- Use `tests.http` with REST Client extension to add books via POST requests.
