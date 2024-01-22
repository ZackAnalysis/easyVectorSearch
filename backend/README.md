# FastAPI Backend

This is the backend part of the application, built with FastAPI.

## Setup and Installation

1. Make sure you have Python 3.8 or later installed.
2. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI application on `localhost:8000`.

## API Endpoints

The application provides the following endpoints:

- `GET /collections`: List all collections in ChromaDB.
- `POST /collections`: Create a new collection in ChromaDB.
- `DELETE /collections/{collection_id}`: Delete a collection from ChromaDB.
- `GET /search/{collection_id}`: Search text in a selected ChromaDB collection.

## Docker

A Dockerfile is provided for building a Docker image of the application. To build the image, use the following command:

```bash
docker build -t my-fastapi-app .
```

To run the application in a Docker container, use the following command:

```bash
docker run -d -p 8000:8000 my-fastapi-app
```

This will start the application in a Docker container and expose it on `localhost:8000`.

## Testing

To run the tests, use the following command:

```bash
pytest
```

This will run all the tests in the `tests` directory.

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes.