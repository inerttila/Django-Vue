# Django-Vue

Private Suggestions Portal collaboratively by utilizing Django Rest Framework 3 for the backend and VueJS 3, with Pinia for the frontend. This platform enables users to submit suggestions and vote, on them. The project is stored in an repository and launching it requires minimal setup. The code is designed to be review friendly facilitating effortless deployment.

## Table of Contents

- [Installation](#installation)
  - [Frontend Installation](#frontend-installation)
  - [Backend Installation](#backend-installation)

## Installation

Clone the repository to your local machine:

```bash
  git clone https://github.com/inerttila/Django-Vue.git
```

```bash
 docker-compose up --build
```

```bash
  cd front
```

Install the required Node.js packages:

```bash
  npm install
```

Start the frontend app:

```bash
  npm run dev
```

## Backend Installation

Open a new terminal and go to the backend directory:

```bash
  cd Django-Vue/reviews
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
