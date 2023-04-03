terraform {
  required_version = "1.3.1"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.43.1"
    }
  }
  backend "gcs" {}
}

variable "gcp" {
  type    = map(string)
  default = {
    project     = ""
    region      = ""
    zone        = ""
    credentials = ""
  }
}

provider "google" {
  project     = var.gcp.project
  region      = var.gcp.region
  zone        = var.gcp.zone
  credentials = var.gcp.credentials
}

locals {
  project_name = "fuilder"
  users_service = "${local.project_name}-users-service"
}

variable "database_password" { type = string }

# ---------------
# Users Service
# ---------------

module "users_service" {
  source = "./modules/services/users_service"

  storage_name     = "${local.users_service}-storage"

  database_instance_name = "${local.users_service}-database"
  database_name          = "${local.users_service}_db"
  database_username      = "${local.users_service}_user"
  database_password      = "${local.users_service}-${var.database_password}"
}

output "users_service_output" {
  value = module.users_service
  sensitive = true
}

