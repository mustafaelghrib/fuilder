# Users Service
A service that responsible for registering, loging and validating users

---

## The Development Environment:

### Run The Backend Locally:
- Copy `.env.sample/.env.development` to `.env/.env.development` and update it.
- Run The Backend API:
  ```shell
  docker compose -f .docker-compose/development.yml up -d --build
  ```

### Run The Tests:
- Run Pytest:
  ```shell
  docker exec -it users_service_development_django /bin/bash -c "/opt/venv/bin/pytest -rP"
  ```
- Run Pytest Coverage:
  ```shell
  docker exec -it users_service_development_django /bin/bash -c "/opt/venv/bin/pytest --cov=."
  ```

## The Production Environment:

### Run The Backend Locally:
- Setup and run the [infrastructure](..%2F..%2Finfrastructure%2FREADME.md)
- Get the environment variables from the infrastructure
- Copy `.env.sample/.env.production` to `.env/.env.production` and update it.
- Run The Backend API:
  ```shell
  docker compose -f .docker-compose/production.yml up -d --build
  ```
  
