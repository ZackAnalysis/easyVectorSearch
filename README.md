# My App

This is a FastAPI and React application that allows users to upload JSON files to ChromaDB and perform text searches in ChromaDB.

## Project Structure

The project is divided into two main parts: the backend and the frontend.

The backend is a FastAPI application that provides API endpoints for managing collections in ChromaDB and performing text searches. It is located in the `backend` directory.

The frontend is a React application that provides a user interface for interacting with the backend. It is located in the `frontend` directory.

## Getting Started

To get started with this application, you need to have Docker and Docker Compose installed on your machine.

### Building the Docker Images

First, navigate to the root directory of the project and build the Docker images using Docker Compose:

```
docker-compose build
```

This will build two Docker images: one for the FastAPI backend and one for the React frontend.

### Running the Application

After the Docker images have been built, you can start the application using Docker Compose:

```
docker-compose up
```

This will start two Docker containers: one for the FastAPI backend and one for the React frontend.

The FastAPI backend will be accessible at `http://localhost:8000`, and the React frontend will be accessible at `http://localhost:3000`.

## Usage

The home page of the application lists the collections in ChromaDB and provides an option to create a new collection. Each collection has a button to delete the collection.

If you choose an existing collection, you will be taken to a new page with a search bar and a search button. You can enter text to search in the collection and choose how many candidates to return (default is 10). The search results will be displayed on the same page, with the content and the score for each result.

If you choose to create a new collection, you will be taken to a new page where you can upload a JSON file (a list of dictionaries) and specify which field in the dictionary should be used as text for embedding. You can also enter a name for the collection. After you submit the form, the data will be sent to the backend to create the collection. Once the collection has been created, you will be redirected back to the home page, and the list of collections will be refreshed.

## Contributing

Contributions are welcome. Please submit a pull request if you have something to add or fix.