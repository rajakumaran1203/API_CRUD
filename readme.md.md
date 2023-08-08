# APIs

This is a Django application that provides APIs for User Registration, Generate Token, store data, Retrieve Data, Update Data, and deleting data.
# Django Project
## Getting Started    
### Prerequisites 
-  Python (3.6 or higher) 
-  Pipenv (recommended for virtual environment management) 
- Docker
- Docker Compose

### Installation and Usage 
 1. Clone this repository: ``bash git clone https://github.com/yourusername/your-django-app.git
 2. **Install Django:** Make sure you have Python and `pip` installed. Then, open your terminal and install Django using pip: ` pip install Django `
 3. **Create a Project:** Choose a name for your project (replace `yourproject` with your desired project name) and create the project using the following command: ` django-admin startproject yourproject `
 4. **Navigate to the Project Directory:** Change your working directory to the newly created project directory: ` cd yourproject `
 
 ## Creating a Django App within the Project: 
 1. **Create an App:** To create a new app (replace `yourapp` with your desired app name), run the following command: ` python manage.py startapp yourapp `
 2. **Add the App to the Project:** Open the `settings.py` file in your project's directory (`yourproject/settings.py`). Find the `INSTALLED_APPS` setting and add your app's name to the list of installed apps:  ` INSTALLED_APPS = [ # ...  'yourapp', # ... ] `
 3.  **Define Models and Views:** Inside your app's directory (`yourapp`), you can define models in the `models.py` file and views in the `views.py` file.
    
4.  **Create URLs for the App:** Create a `urls.py` file within your app's directory (`yourapp`). Define URL patterns specific to your app in this file.
## Database SQL Lite
**Migrate Database Changes:** After defining models, run migrations to apply database changes: ` python manage.py makemigrations yourapp python manage.py migrate `
 
## Instructions to run the code
## API Endpoints

### User Registration

-   Endpoint: `POST /api/register`
-   Request: ` {"username": "example_user","email": "user@example.com",  "password": "secure_password123",
  "full_name": "John Doe",  "age": 30,  "gender": "male" }
`
-   Success Response: ` {
  "status": "success",  "message": "User successfully registered!",  "data": {  "user_id": "12345",  "username": "example_user", "email": "user@example.com", "full_name": "John Doe","age": 30, "gender": "male"  }}
 `
-   Error Response: ` {  "status": "error",  "code": "INVALID_REQUEST",
  "message": "Invalid request. Please provide all required fields: username, email, password, full_name."} `

### Generate Token

-   Endpoint: POST /api/token
-   Request : ` {  "username": "example_user",  "password": "secure_password123"}  `
-   Response: ` {  "status": "success",
  "message": "Access token generated successfully.",
  "data": {    "access_token": "<TOKEN>",    "expires_in": 3600
  }} `

### Store Data

-   Endpoint: `POST /api/data`
-   Request Headers: `Authorization: Bearer access_token`
-   Request Body: ` { "key": "unique_key",  "value": "data_value" }`
-   Response: ` {  "status": "success", "message": "Data stored successfully." } `

### Retrieve Data

-   Endpoint: `GET /api/data/{key}`
-   Request Headers: `Authorization: Bearer access_token`
-   Response: `{ "status": "success",  "data": { "key": "unique_key", "value": "data_value"  } } `

### Update Data

-   Endpoint: `PUT /api/data/{key}`
-   Request Headers: `Authorization: Bearer access_token`
-   Request Body: { "value": "new_data_value" }
-  Response:  ` { "status": "success", "message": "Data updated successfully."}  `

### Delete Data

-   Endpoint: `DELETE /api/data/{key}`
-   Request Headers: `Authorization: Bearer access_token`
-   Response: ` { "status": "success", "message": "Data deleted successfully."} `



## Instructions to setup the code.
 1. Navigate to the project directory: ` cd User_Details `
 2. Install project dependencies using Pipenv (or your preferred method): ` pipenv install `
 3. Create a `.env` file in the project directory and add your environment variables:  ` DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost or IP  
DATABASE_URL=postgres://postgres:postgres@db:5432/yourdb `
 3. Build and start the services using Docker Compose: ` docker-compose up --build `
 4. Apply database migrations: ` pipenv run python manage.py migrate `
 5. Create a superuser (admin) for the Django admin interface: ` pipenv run python manage.py createsuperuser `
 6. Start the development server: ` pipenv run python manage.py runserver `
 7. Access the Django admin interface at `http://localhost:8000/admin` using the superuser credentials.


```
