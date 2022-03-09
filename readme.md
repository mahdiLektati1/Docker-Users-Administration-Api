# Flask + React + MySQL Docker Rest API

Building RESTFul API Services using Flask, MySQL, Nginx and Swagger Documentation with containerization using Docker

Steps for executing :

1. Clone/Download the repository.

2. Open the terminal and go to the directory where docker-compose.yml is located and run the below command. It will build the MySQL - Nginx and Flask Rest API Containers.

     docker-compose up

3. Run the below command to get the list of running containers :

    docker ps

4. After executing above steps without any errors and docker containers are up and running, open the browser and navigate to below url:

    - Swagger API documentation : <http://localhost:8000/swagger>

    - PHPMyAdmin : <http://localhost:8080>
        - user      : root
        - password  : password  

**Project Structure**

We will create a user administration API. Where API clients can add new users and see users added by others. We will have a MySQL database to store users, a backend API using Flask and Flask Restful, and Docker to have an environment independent API.

We have the following folders: api, nginx and db. The db folder contains the sql query to create the user table. The api folder contains the code for our Flask API and the nginx folder contains our nginx configurations.

**Docker**

The docker-composer file contains our docker configuration.

First, we created a service called db. This is the database container where we tell docker-composer to build an image of mysql version 5.7.
The volume line copies the contents of the db folder to /docker-entrypoint-initdb.d. All sql files in the folder are executed. Therefore, the database, table and data in db/init.sql will be created in the container.
Then we tell docker-compose to always restart the container when we rebuild it.
We also make sure to set the environment variables for the database used by the container.
For data consistency, we also added a mysql-data volume to keep track of changes in the database.

We use PHPMyAdmin to access and manage our database in the container.
The last line of the phpmyadmin service has ports set to 8080:80. The first port is the port of the host computer. The second port is the port on which the service is running in the container. This means that if we go to localhost:8080 on the browser, we should be able to access localhost (port 80) in the container where phpmyadmin will be running.

Then the flask API, we have a Dockerfile where we specify the version of python we are using and set up the working directory with the dependency installation via the requirements file. We use uwsgi to run the application which is a hosting service.

The api service instance listens on port 9000 inside the container but we will access it on our host machine (outside the container) on port 8000.

Finally, we have the Nginx service with a conf file to specify that we listen on port 8000 and direct it to api:9000. This is because containers use the service name as the host name. In the docker-compose file, the api service is called "api" and runs on port 9000. Therefore, to access it in the container, we go to api:9000.

**Troubleshooting**

1. Any errors related to "connection link failure" is seen while starting/running containers then it might be due to the  MySQL hostname use in the application database connection. Run the below command to get the hostname of the MySQL and replace it

      docker inspect {CONTAINER-ID}
