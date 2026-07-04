# AI Site

A beginner-friendly Django portfolio project with articles, a simple market, user accounts, profiles, a contact form, and a session-based cart.

## Features

- Article listing, detail pages, creation, editing, comments, images, and view counts
- Product listing, detail pages, creation, reviews, images, and session cart checkout
- User registration, login, logout, profile, and profile editing
- Contact form stored in the Django admin
- Bootstrap 5 templates with responsive pages

## Tech Stack

- Python
- Django
- SQLite for local development
- Bootstrap 5 and Bootstrap Icons

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Environment Variables

Create a `.env` file or set environment variables in your shell for production-style settings:

```bash
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
```

## Notes

Uploaded media files are stored in `media/` during development. Static files are served from `static/` locally and collected into `staticfiles/` for deployment.
