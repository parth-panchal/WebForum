#!/bin/bash

# Install Python and pip
# sudo apt-get update
# sudo apt-get install python3 python3-pip -y

# # Install virtualenv
pip install virtualenv

# # Create and activate a virtual environment
virtualenv venv
source venv/bin/activate

# Install Django
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations onlineforum
python manage.py migrate
python manage.py create_superuser
