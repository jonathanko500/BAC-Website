Website live from 11/2023 - 05/2025

Project setup
=================

Project setup instruction here.

Need Python installed in machine

1. Clone the project from git.
2. Install the dependencies in requirements.txt.
3. Run the project.

| Terminal Commands                 | Reason                                                      |
|-----------------------------------|-------------------------------------------------------------|
| `pip install -r requirements.txt` | Install dependencies from requirements.txt                  |
| `python manage.py runserver`      | Run the Django project. Access development site [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| `python manage.py makemigrations` | Create new migrations based on the changes detected to your models |
| `python manage.py migrate`        | Apply the migrations to the database                        |
| `python manage.py collectstatic`  | Collect static files into STATIC_ROOT                       |
| `python manage.py startapp <app_name>` | Create a new Django app                                     |
