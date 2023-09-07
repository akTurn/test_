1.Introduction:

This is the documentation for the Chess_moves API project.It provides information on how to use the API to determine valid moves for various
chess pieces,including Knight, Rook, Bishop, and Queen.

2.Getting Started:

Prerequisites

 # Make sure  Docker and Python installed on the system.

 # Clone the repository

 git clone https://AK_2023@bitbucket.org/ak2023-api/trialrepo.git

 #Run the Docker Container

   Build the Docker image and run the container:

   docker build -t chess-api .
   docker run -p 8000:8000 chess-api


3.Test the API:

Start Your Dockerized API:
Make sure your Dockerized Chess API is running.

Create a New Request:
Open Postman and click the "New" button to create a new request.

Set Request Details:

Request Type: Choose the HTTP request type (e.g., POST).
URL: Enter the API endpoint URL. For example: http://localhost:8000/chess/knight
Headers: You may need to set headers depending on your API requirements. Typically, no additional headers are required for this type of API.
Body: Select the "raw" option and set the body to JSON format.

Input JSON:
Provide the input JSON data in the request body. For example:
{
  "Positions": {
    "Queen": "E7",
    "Bishop": "B7",
    "Rook": "G5",
    "Knight": "C3"
  }
}
Send the Request:
Click the "Send" button to send the request to your API.

View the Response:
Postman will display the API response in the lower part of the window.
You should see the valid moves for the specified chess piece.

Repeat the above steps for different endpoints (/chess/knight, /chess/rook, /chess/bishop, /chess/queen) to test various chess piece movements.

Ensure that API is running and properly configured to accept requests from Postman.
you can use the provided input examples and check if the responses match the
expected output.

