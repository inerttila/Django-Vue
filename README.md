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

Navigate to the project directory:

```bash
  cd Django-Vue
```

## Frontend Installation

To run the Vue app, navigate to the front-end directory:

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

Create and activate a virtual environment:

```bash
  pip install pipenv
  pipenv install
```

Start the environment:

```bash
  pipenv shell
```

Create a superuser for the Django project:

```bash
  python manage.py createsuperuser
```

Run the Django project:

```bash
  python manage.py runserver
```
