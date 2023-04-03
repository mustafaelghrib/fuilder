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
}
