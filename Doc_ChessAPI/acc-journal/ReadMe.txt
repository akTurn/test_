/*
Build the Docker Image:

docker build -t my-mysql-image .

Run the MySQL Container:

docker run -d --name my-mysql-container -e MYSQL_ROOT_PASSWORD=root_password -p 3306:3306 my-mysql-image

Run  Application Container:

docker run -d --name my-app-container --link my-mysql-container my-app-image
*/
To run your Flask application inside the Docker container, you can follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory containing your `docker-compose.yml` file.

3. Run the following command to start your Docker services defined in the `docker-compose.yml` file:

   ```bash
   docker-compose up
   ```

   This command will build the Docker images and start the containers for your Flask application and MySQL database, based on the configurations in the `docker-compose.yml` file.

4. Once the containers are up and running, you can access your Flask application in a web browser by going to `http://localhost:8000`. Your Flask application should be running on port 8000, as specified in the `docker-compose.yml` file.

5. To stop the running containers, you can press `Ctrl + C` in the terminal where you ran `docker-compose up`. This will gracefully stop the containers.

If you want to run the containers in the background (detached mode), you can add the `-d` flag to the `docker-compose up` command like this:

```bash
docker-compose up -d
```

With this, the containers will continue running in the background, and you can stop them later using the `docker-compose down` command:

```bash
docker-compose down
```

Please make sure you have Docker and Docker Compose installed and configured correctly on your system for this to work.



