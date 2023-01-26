# File Checker

File Checker is a Django project that allows users to upload or provide a URL for a file and checks the hex header against a MySQL database to determine the file type. This is a project for a Objectoriented Script Languages college course. 

## Prerequisites

- Python 3.x
- Django 3.x
- MySQL

## Database 

For the creation of the DB a list of file signatures from https://www.garykessler.net/library/file_sigs.html was used. 

## Installation

1. Clone the repository

git clone https://github.com/<username>/file-checker.git

2. Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate

3. Install the required packages

pip install -r requirements.txt

4. Create a .env file in the root of the project and set the following environment variables:

SECRET_KEY=<your_secret_key>

DEBUG=True

ALLOWED_HOSTS=127.0.0.1, .localhost

MYSQL_ADDON_HOST=host

MYSQL_ADDON_DB=dbname

MYSQL_ADDON_USER=user

MYSQL_ADDON_PORT=port

MYSQL_ADDON_PASSWORD=password

5. Run the migrations to create the necessary database tables.

python manage.py makemigrations
python manage.py migrate

## Running the project

1. Start the development server

python manage.py runserver

2. Open the application in your browser at http://127.0.0.1:8000/

## Deployment

To deploy File Checker to a production environment, you will need to set the DEBUG environment variable to False, and set the ALLOWED_HOSTS environment variable to the domain name of your server.
