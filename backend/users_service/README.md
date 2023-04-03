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
