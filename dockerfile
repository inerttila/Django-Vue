# Stage 1: Build the Vue.js frontend
FROM node:20 AS frontend

WORKDIR /usr/src/app
WORKDIR /usr/src/app/front
COPY front/package*.json ./
RUN npm install

COPY front/ ./
RUN npm run build

# Stage 2: Prepare the Django backend
FROM python:3.9-slim AS backend

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    curl \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

COPY --from=frontend /usr/src/app/front/dist /usr/src/app/front/dist

RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

COPY reviews/ ./reviews

WORKDIR /usr/src/app/reviews

RUN pip install djangorestframework django-cors-headers


COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8000 3000

CMD ["sh", "-c", "python manage.py migrate && supervisord -c /etc/supervisor/conf.d/supervisord.conf"]
