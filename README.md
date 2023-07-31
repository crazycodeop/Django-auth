# Django Authentication API with JWT Token

This project is a Django-based Authentication API that provides essential features such as login, register, change password, and reset password. The API uses JSON Web Tokens (JWT) for secure authentication.

## Features

- User registration with email and password
- User login to obtain JWT tokens for authentication
- Change password functionality
- Reset password functionality with email confirmation
- Secure authentication using JWT tokens

## Requirements

Make sure you have the following installed before running the API:

- Python (>= 3.6)
- Django (>= 3.x)
- Django Rest Framework (>= 3.x)
- djangorestframework-simplejwt

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-auth-api.git
   cd django-auth-api
   ```

2. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `PUT /api/change-pass/` - Change user password (requires authentication)
- `POST /api/reset-pass/` - Request password reset (email confirmation)
- `POST /api/reset-pass/<uid>/<token>` - Confirm password reset and change password

## Contributing
Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.
