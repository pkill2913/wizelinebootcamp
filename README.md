# API App

This app has two APIs, the first is the traditional hello world, and the second is another API for getting info about your IP.

This application is containerized with Docker, so to run you have to run the Dockerfile first.

This project has 2 files:

* app.py is the python app: Code with the project.
* Dockerfile: File for creating image.
* requirements.txt: File with modules needed to run the app.

# For run application

Requirements:

Docker installed.

Run:

`docker build -t app:python .` 

`docker run --name application_oscar_castillo -p 80:5000 app:python`

You can change the port from 80 to whatever ( not in use for another app ), but 5000 is required

Access application open a browser and use the URL

http://127.0.0.1/hworld

Is hello world application

http://127.0.0.1/info

Retrieve info for other API that gets information about from your public IP.