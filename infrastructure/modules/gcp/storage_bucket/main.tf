terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
  }
}
variable "storage_name" { type = string }
variable "storage_location" { type = string }

resource "google_storage_bucket" "main" {
  name          = var.storage_name
  location      = var.storage_location
  force_destroy = true
}

output "GS_BUCKET_NAME" { value = var.storage_name }
