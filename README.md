---

# 🚀 Frontend and Testing Guide

## Running the Front-End

The FastAPI application serves the web interface found in the `templates/` directory.
After installing the dependencies from `requirements.txt`, launch the server with:

```bash
uvicorn app.main:app --reload
```

Visit <http://localhost:8000> in your browser to access the frontend.
You can also start the entire stack using Docker Compose:

```bash
docker-compose up --build
```

## Running Playwright Tests

End-to-end tests rely on Playwright. Install the browsers and run the tests with:

```bash
playwright install
pytest tests/e2e/
```

These tests open a headless browser and interact with the application.

## Docker Hub Image

Container images for this project are published to Docker Hub under
https://hub.docker.com/r/thanna96/assignment14.
Pull and run the latest image using:

```bash
docker pull thanna96/assignment14:latest
docker run -p 8000:8000 thanna96/assignment14:latest
```