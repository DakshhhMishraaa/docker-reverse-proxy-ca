# Docker Networking and Reverse Proxy with Internal Routing

## Project Overview

This project implements a containerized e-commerce backend using Docker Compose, Nginx as a reverse proxy, three FastAPI microservices, and a PostgreSQL database.

The application demonstrates reverse proxy routing, internal Docker networking, service-to-database communication, persistent storage, automated testing, and CI using GitHub Actions.

## Architecture

The system consists of five containers:

1. **Nginx:** Routes incoming HTTP requests to the appropriate backend service.
2. **Users API:** Retrieves user records from PostgreSQL.
3. **Products API:** Retrieves product records from PostgreSQL.
4. **Orders API:** Retrieves order records from PostgreSQL.
5. **PostgreSQL:** Stores application data persistently.

## Technology Stack

- Docker and Docker Compose
- Nginx
- Python and FastAPI
- PostgreSQL 16
- psycopg2-binary
- Pytest and Requests
- GitHub Actions

## Request Routing

The application is accessible through `http://localhost:8080`.

| Endpoint | Service | Database table |
|---|---|---|
| `/users/` | Users API | `users` |
| `/products/` | Products API | `products` |
| `/orders/` | Orders API | `orders` |

Nginx forwards requests to the corresponding service over the internal Docker network.

## Docker Networking

Two Docker bridge networks are configured:

- **proxy-network:** Connects Nginx to the proxy-facing network.
- **backend-network:** An internal network connecting Nginx, the APIs, and PostgreSQL.

The backend network uses Docker's `internal: true` setting to restrict external connectivity. Backend services do not publish their ports to the host; they expose port 8000 internally.

Nginx publishes port 80 inside the container as port 8080 on the host.

## Database Integration

The three FastAPI services connect to PostgreSQL using `psycopg2-binary`.

- The Users API queries the `users` table.
- The Products API queries the `products` table.
- The Orders API queries the `orders` table.

Database credentials are supplied through environment variables and a local `.env` file. The `.env` file must not be committed to version control.

A Docker named volume, `postgres-data`, preserves database data across container recreation.

The database health check uses `pg_isready`. The API services depend on the database becoming healthy before starting.

If a database query fails, the API returns an HTTP 503 response.

## API Health Endpoints

Each service also provides a `/health` endpoint that returns its service name and a healthy status.

## Testing

Automated tests are implemented in `tests/test_services.py` using Pytest and Requests.

Run the tests locally with:

```powershell
python -m pytest -v
```

The current test suite contains three tests, one for each API service.

**Latest local test result:** 3 passed.

## Continuous Integration

GitHub Actions runs the project's automated checks. The workflow builds and starts the services, waits for them to become available, executes the tests, collects logs if a failure occurs, and cleans up the Docker environment.

## Running the Project

Ensure Docker Desktop is running and the local `.env` file contains the required database credentials.

Start the application:

```powershell
docker compose up -d --build
```

Check container status:

```powershell
docker compose ps
```

Validate the Compose configuration:

```powershell
docker compose config --quiet
```

Test the APIs:

```powershell
Invoke-RestMethod http://localhost:8080/users/
Invoke-RestMethod http://localhost:8080/products/
Invoke-RestMethod http://localhost:8080/orders/
```

Stop the application:

```powershell
docker compose down
```

The named database volume is retained when using `docker compose down`. Do not use `docker compose down -v` unless you intentionally want to delete the persisted database volume.

## Learning Outcomes

- Configuring reverse proxy routing with Nginx.
- Creating isolated Docker networks.
- Deploying multiple services using Docker Compose.
- Connecting FastAPI applications to PostgreSQL.
- Managing environment-based configuration and persistent storage.
- Testing API endpoints with Pytest.
- Automating validation through GitHub Actions.