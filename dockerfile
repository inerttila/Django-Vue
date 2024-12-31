# Stage 1: Build the Vue.js frontend
FROM node:20 AS frontend

WORKDIR /usr/src/app

# Install Node.js using nvm and build the frontend
RUN apt-get update && apt-get install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash \
    && export NVM_DIR="$HOME/.nvm" \
    && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" \
    && nvm install node

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

RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

WORKDIR /usr/src/app/reviews
COPY reviews/ ./

RUN pip install djangorestframework django-cors-headers

# Copy the frontend build into the backend container
COPY --from=frontend /usr/src/app/front/dist /usr/src/app/reviews/static

COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN python manage.py migrate

EXPOSE 8000 3000

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]