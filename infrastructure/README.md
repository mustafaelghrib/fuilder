# Fuilder Infrastructure
Fuilder infrastructure is built on Google Cloud Platform (GCP) using Terraform

## Setup Terraform Backend and Secrets:
- Create new project and get the project id
- Create a GCP storage and get the bucket name
- Download a service key file and rename it to `.gcp_creds.json`
- Copy `.backend.hcl.sample`, rename it to `.backend.hcl`, and update it.
- Copy `.secrets.auto.tfvars.sample`, rename it to `.secrets.auto.tfvars`, and update it.


## Run Terraform Commands:
- Create alias for terraform command
  ```shell
  alias TERRAFORM="docker compose -f .docker-compose.yml run --rm terraform"
  ```
- terraform init
  ```shell
  TERRAFORM init -backend-config=.backend.hcl
  ```

---
