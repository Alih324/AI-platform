# AI Platform

A modular full-stack web application built with Django that combines a blogging system, an online marketplace, user authentication, and contact management into a single platform.

## About the Project

AI Platform is a Django-based web application that demonstrates the implementation of multiple real-world web application features within a single project. Instead of focusing on one functionality, the platform integrates article publishing, an online marketplace, user account management, and a contact system while following Django's modular architecture.

Users can create accounts, authenticate securely, manage their profiles, publish and browse articles, upload images, leave comments and reviews, browse products, add items to a session-based shopping cart, and communicate through a contact form. The project also provides an administrative interface through Django Admin for managing users, products, articles, and contact messages.

The application follows Django's recommended project structure, separating each feature into independent applications, making the project easier to maintain, extend, and scale.

The primary goal of this project is to demonstrate practical backend development skills using Django, including authentication, CRUD operations, database modeling, session management, file uploads, responsive frontend development, and clean project organization.

## Features

### Authentication
- User registration
- Login and logout
- User profile
- Profile editing

### Articles
- Create articles
- Edit articles
- Delete articles
- Article images
- Comments
- View counter

### Marketplace
- Product listing
- Product publishing
- Product details
- Product reviews
- Product image uploads
- Session-based shopping cart

### Contact
- Contact form
- Messages managed through Django Admin

### Interface
- Responsive Bootstrap 5 UI
- Mobile-friendly layout
- Bootstrap Icons

## Technology Stack

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons

## Project Structure

```
ai_platform/
├── users/          # Authentication and user profiles
├── articles/       # Blogging system
├── market/         # Marketplace and shopping cart
├── contact/        # Contact form and messages
├── core/           # Shared/core app logic
└── media/          # Uploaded images and files
```

Each Django application is responsible for a separate part of the system, following a modular architecture for better maintainability.

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd ai-platform
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for Django Admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser.

## License

Add your license information here.
