# FastAPI SpaCy Similarity API

This project provides an API to calculate text similarity using FastAPI and spaCy.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Build and start the application using Docker Compose:

    ```sh
    docker-compose up --build
    ```

2. The API will be available at `http://localhost:8000`.

### API Endpoints

#### Calculate Text Similarity

- **Endpoint:** `/similarity`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "statement": "I love you",
    "sentences": [
      "I like you",
      "You are amazing",
      "I love ice cream"
    ]
  }


Response:
```json
{
  "statement": "I love you",
  "results": [
    {
      "sentence": "I like you",
      "similarity": 0.8
    },
    {
      "sentence": "You are amazing",
      "similarity": 0.5
    },
    {
      "sentence": "I love ice cream",
      "similarity": 0.85
    }
  ]
}

```
Example : 

```code
 curl -X POST http://localhost:8000/similarity -H "Content-Type: application/json" -d '{"statement": "I love you", "sentences": ["I like you", "You are amazing", "I love ice cream"]}'
