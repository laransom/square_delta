# Square Delta Server

This README outlines the details for building and deploying Square Delta

## Installation

* Download project
* change into project directory
* pip install -r requirements
* Run postgres
* python manage.py migrate

## Running Client
* python manage.py runserver 0.0.0.0:8001 (Default is 8000. Application won't connect to the client unless it's on 8001)

## Usage
* localhost:8000/difference?number=n where n is any integer greater than - and less than or equal to 100
* return will be JSON
