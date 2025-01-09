FROM python:3.9-slim
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*
COPY . .
RUN pip install djangorestframework django-cors-headers
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]