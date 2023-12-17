#!/bin/bash

# Install Python and pip
# sudo apt-get update
# sudo apt-get install python3 python3-pip -y

# # Install virtualenv
# pip install virtualenv

# # Create and activate a virtual environment
# virtualenv venv
# source venv/bin/activate

# Install Django
echo "Installing requirements..."
exec pip install -r requirements.txt

# Run database migrations
echo "Running migrations..."
exec python manage.py makemigrations onlineforum

echo "Migrating"
exec python manage.py migrate

echo "Creating superuser"
exec python manage.py create_superuser
