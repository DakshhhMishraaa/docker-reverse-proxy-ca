# Docker Networking + Reverse Proxy — Internal Routing

## 1. Project Overview

This project demonstrates a multi-service web application deployed using Docker Compose, with Nginx configured as a reverse proxy to route incoming HTTP requests to individual backend services.

The application consists of three FastAPI services — Users, Products, and Orders — alongside a PostgreSQL database. Docker networking enables communication between services, while Nginx provides a single entry point for accessing the APIs.

The project also includes automated API tests using Pytest and a GitHub Actions workflow for Continuous Integration (CI).

## 2. Objectives

- Deploy multiple services using Docker Compose.
- Configure Nginx as a reverse proxy for internal service routing.
- Implement separate Docker networks for proxy-facing and backend communication.
- Configure PostgreSQL with database initialization and persistent storage.
- Test API endpoints using automated tests.
- Automate testing through GitHub Actions.

## 3. Technologies Used

- **Docker and Docker Compose:** Containerization and multi-service orchestration.
- **Nginx:** Reverse proxy and HTTP request routing.
- **Python and FastAPI:** Backend REST API services.
- **PostgreSQL:** Relational database.
- **Pytest and Requests:** Automated API testing.
- **Git and GitHub:** Version control and repository hosting.
- **GitHub Actions:** Continuous Integration workflow.

## 4. Project Structure

```text
docker-reverse-proxy-ca/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_services.py
├── nginx/
│   └── nginx.conf
├── users/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── products/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── orders/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── database/
│   └── init.sql
├── docker-compose.yml
├── requirements-test.txt
├── .gitignore
└── README.md
```

A root-level `.env` file is also used for local database configuration and is excluded from Git.

## 5. Application Architecture

The application contains five containers:

1. **Nginx:** Receives incoming HTTP requests on port 8080 and routes them to the appropriate backend service.
2. **Users API:** Provides the Users endpoint.
3. **Products API:** Provides the Products endpoint.
4. **Orders API:** Provides the Orders endpoint.
5. **PostgreSQL:** Hosts the database and its initialized tables.

### Request Routing

| Endpoint | Destination |
|---|---|
| `/users/` | Users API |
| `/products/` | Products API |
| `/orders/` | Orders API |

The Nginx container listens on port 80 internally, mapped to port 8080 on the host machine. Backend APIs listen on port 8000 within their containers.

## 6. Docker Networking

The project uses two Docker networks:

- **proxy-network:** Connects Nginx with the backend API services for request routing.
- **backend-network:** Provides an internal network for backend communication, including database access.

A Docker named volume, `postgres-data`, is configured to preserve PostgreSQL data beyond the lifetime of an individual container.

## 7. Environment Configuration

Create a `.env` file in the project root with the following local development settings:

```dotenv
POSTGRES_USER=admin
POSTGRES_PASSWORD=replace_with_a_local_password
POSTGRES_DB=ecommerce
```

Replace the password placeholder with your own local development password. Do not commit `.env` or real credentials to GitHub.

The Compose configuration uses these variables to configure PostgreSQL.

## 8. Running the Application

### Prerequisites

- Docker Desktop installed and running.
- Git installed.
- Python installed if running the test suite directly on the host.

### Start the containers

Open a terminal in the project directory and run:

```powershell
docker compose up -d --build
```

### Verify the containers

```powershell
docker compose ps
```

### Access the APIs

Open the following URLs in a browser:

- Users: http://localhost:8080/users/
- Products: http://localhost:8080/products/
- Orders: http://localhost:8080/orders/

Health endpoints are also configured for the individual services at `/health` within each service.

### View logs

```powershell
docker compose logs
```

### Stop the application

```powershell
docker compose down
```

The named PostgreSQL volume is retained when the containers are stopped using this command.

## 9. Database Configuration

PostgreSQL is configured through Docker Compose. The initialization script at `database/init.sql` defines the database tables and seed data.

The database contains the following tables:

- `users`
- `products`
- `orders`

To list the tables:

```powershell
docker compose exec database psql -U admin -d ecommerce -c "\dt"
```

To inspect user records:

```powershell
docker compose exec database psql -U admin -d ecommerce -c "SELECT * FROM users;"
```

**Implementation note:** The current API implementations return hardcoded sample responses. Although PostgreSQL is configured and initialized, direct database queries from the API services have not been implemented or verified.

## 10. Automated Testing

The project includes automated tests in `tests/test_services.py` to verify that the Users, Products, and Orders endpoints return successful HTTP responses and expected JSON fields.

Install the test dependencies:

```powershell
python -m pip install -r requirements-test.txt
```

Run the test suite while the application is running:

```powershell
python -m pytest -v
```

All three API tests have passed in the local environment.

## 11. Continuous Integration with GitHub Actions

The workflow is defined in `.github/workflows/ci.yml`.

The CI pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs testing dependencies.
4. Builds and starts the Docker Compose services.
5. Waits for the application endpoints to become available.
6. Executes the automated API tests.
7. Displays service logs if a failure occurs.
8. Stops the application services.

The workflow runs on pushes to the `main` branch and pull requests targeting `main`.

**Verification:** The latest GitHub Actions workflow run completed successfully, including automated tests and cleanup.

## 12. Repository

GitHub: https://github.com/DakshhhMishraaa/docker-reverse-proxy-ca

## 13. Conclusion

This project demonstrates containerized deployment, reverse proxy configuration, service discovery through Docker networking, PostgreSQL initialization, automated API testing, and Continuous Integration using GitHub Actions.

It provides a foundation for deploying and testing a multi-service web application using a reproducible Docker-based environment.
