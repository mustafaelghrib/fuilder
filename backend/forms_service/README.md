# Forms Service
A service that responsible for managing forms

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
  docker exec -it forms_service_development_django /bin/bash -c "/opt/venv/bin/pytest -rP"
  ```
- Run Pytest Coverage:
  ```shell
  docker exec -it forms_service_development_django /bin/bash -c "/opt/venv/bin/pytest --cov=."
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

### Deploy Manually on Minikube with Docker and Kubernetes:
- Export Values:
  ```shell
  export ENVIRONMENT=production;
  export PROJECT_NAME=fuilder-forms-service;
  export DOCKER_HUB=mustafaabdallah;
  export FINAL_IMAGE=$DOCKER_HUB/$PROJECT_NAME
  ```
- Build a Docker Image:
  ```shell
  docker build -t $FINAL_IMAGE . --build-arg ENVIRONMENT=$ENVIRONMENT
  ```
- Push to Docker Hub:
  ```shell
  docker push $FINAL_IMAGE
  ```
- Run The Image Locally:
  ```shell
  docker run -d -p 80:8000 --env-file .env/.env.production $FINAL_IMAGE \
  /bin/bash -c "chmod +x ./entrypoint.sh && sh ./entrypoint.sh"
  ```
- Deploy to Kubernetes
  ```shell
  kubectl create secret generic "$PROJECT_NAME-env-secrets" --from-env-file=.env/.env.production
  kubectl apply -f .kubernetes/deployment.yml
  kubectl apply -f .kubernetes/service.yml
  ```
- Launch the app
  ```shell
  minikube service $PROJECT_NAME
  ```

---
