## Backend Installation

### Setup Python Virtual Environment

Open a new terminal and navigate to the backend directory:

```bash
  cd Inventory-Management/reviews
```

```bash
python -m venv env

.\env\Scripts\activate
```

Install Django Packages

```bash
  pip install djangorestframework django-cors-headers
```

```bash
  python manage.py migrate
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
