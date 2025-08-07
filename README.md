---
# Calculator Web Application

A full-stack description covers both client-side (frontend) and server-side (backend) layers, alongside database and communication details.

---

## Application Name
**Calculator Web App**

## Purpose
Allow users to register, authenticate, and perform basic arithmetic (addition, subtraction, multiplication, division) while storing, viewing, editing, and deleting past calculations.

---

## Frontend (Client-Side)
- **Technologies:** Jinja2 templates, HTML5, Tailwind CSS for styling, vanilla JavaScript for interactions. Tailwind and custom styles are loaded in the shared layout template.
- **Features:** Responsive pages for index, registration, login, and dashboard; dynamic dashboard listing calculations and accepting new ones; token-based session management via browser storage.

## Backend (Server-Side)
- **Technologies:** FastAPI with Jinja2 templates and static file serving, SQLAlchemy for ORM, Uvicorn ASGI server.
- **Features:** BREAD-style endpoints for calculations, user registration and login, JWT-based authentication settings, and startup tasks that initialize database tables.

---

## Database
- **Technology:** PostgreSQL accessed through SQLAlchemy. Default connection string targets a local Postgres instance.
- **Schema:** Users table with fields for credentials and profile data, plus relationships to a polymorphic `Calculations` table where inputs are stored as JSON and results as floats.

---

## Communication
- **Protocol & Format:** RESTful HTTP endpoints returning JSON; client scripts call these endpoints with `fetch`.
- **Authentication:** OAuth2 with JWT tokens; tokens saved client-side and included in API requests.

---

## Deployment & Version Control
- **Deployment:** Dockerfile and docker-compose orchestrate a web container and Postgres database, wiring environment variables and health checks for development or deployment.
- **Version Control:** Git repository intended for collaborative development.
- **Testing:** Pytest for unit/integration tests and Playwright for end-to-end browser tests, as outlined below.

---

# Frontend and Testing Guide

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