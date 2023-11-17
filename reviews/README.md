## Backend Installation

### Setup Python Virtual Environment

Open a new terminal and navigate to the backend directory:

```bash
  cd Django-Vue/reviews
```

Install Pipenv (if not already installed):

```bash
  pip install pipenv

```

Create and activate the Python virtual environment:

```bash
  pipenv install
  pipenv shell
```

Install Django Packages

Install the required Python packages using Pipenv:

```bash
  pipenv install djangorestframework django-cors-headers
```

Create a superuser for the Django project:

```bash
  python manage.py createsuperuser
```

```bash
  python manage.py runserver
```

<!--  pip install djangorestframework
      pip install django-cors-headers
   -->
