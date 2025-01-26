## HOW TO USE...

## Installation

1. Clone the repository:

   git clone git@github.com:ramin971/TODO_Application.git
   


2. Install the required dependencies:

   pip install -r requirements.txt
   


3. Set up the database:
   
   python manage.py makemigrations
   python manage.py migrate
   


4. Create a superuser for accessing the Django admin panel:

   python manage.py createsuperuser
   


5. Run the development server:

   python manage.py runserver
   

## SWAGGER DOCUMENTATION

6. Access the Swagger UI documentation at `http://localhost:8000/api/schema/swagger-ui/` to explore the API endpoints.

## Authentication

- JWT authentication is used for securing the API endpoints.
- To obtain a JWT token, send a POST request to `http://localhost:8000/api/auth/jwt/create/` with your username and password.
- Include the JWT token in the Authorization header of your requests as `Bearer <token>`.

## API Endpoints

- `/api/auth/users/`: Create a new User and receiving JWT token by providing username and password and email.
- `/api/auth/jwt/create/`: Obtain JWT token by providing username and password.
- `/api/auth/jwt/refresh/`: Refresh JWT token.
- `/api/todoitems/`: List all your todo items or create a new todo item.
- `/api/todoitems/<id>/`: Retrieve, update, or delete a specific todo item that belong to you.
