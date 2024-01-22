# Frontend

This is the frontend of our application, built with React.

## Setup

First, make sure you have Node.js and npm installed on your machine. You can download Node.js and npm from here: https://nodejs.org/en/download/

After installing Node.js and npm, navigate to the frontend directory:

```
cd frontend
```

Then, install the dependencies:

```
npm install
```

## Running the App

To start the app, run:

```
npm start
```

The app will run on http://localhost:3000 by default.

## Building the App

To build the app for production, run:

```
npm run build
```

This will create a `build` directory with the production-ready app.

## Docker

A Dockerfile is provided if you prefer to build a Docker image of the frontend. To build the image, navigate to the frontend directory and run:

```
docker build -t my-app-frontend .
```

Then, to run the container, use:

```
docker run -p 3000:3000 my-app-frontend
```

The app will be accessible at http://localhost:3000

## Components

The app consists of several components:

- `CollectionList.js`: Displays the list of collections in ChromaDB and options to create or delete a collection.
- `CollectionCreate.js`: Provides a form for creating a new collection in ChromaDB.
- `CollectionSearch.js`: Provides a search bar for searching text in a selected ChromaDB collection.
- `SearchResults.js`: Displays the search results from a ChromaDB collection.

## Styles

The app's styles are located in the `src/styles` directory. The main stylesheet is `App.css`.

## API

The `src/utils/api.js` file contains utility functions for making API requests to the FastAPI backend.