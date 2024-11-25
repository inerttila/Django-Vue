#!/bin/bash

# Path to your database file
DB_PATH="/data/db.sqlite3"

# Check if the database file exists
if [ ! -f "$DB_PATH" ]; then
  echo "Database not found at $DB_PATH. Running migrations to create it..."
  python manage.py migrate
else
  echo "Database found at $DB_PATH. Skipping migrations..."
fi

# Start the Django development server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
