terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
  }
}
variable "database_instance_name" { type = string }
variable "database_version" { type = string }
variable "database_tier" { type = string }
variable "database_name" { type = string }
variable "database_username" { type = string }
variable "database_password" { type = string }

resource "google_sql_database_instance" "main" {
  name                = var.database_instance_name
  database_version    = var.database_version
  deletion_protection = false
  settings {
    tier = var.database_tier
  }
}

resource "google_sql_database" "main" {
  name     = var.database_name
  instance = google_sql_database_instance.main.name
}

resource "google_sql_user" "main" {
  name     = var.database_username
  password = var.database_password
  instance = google_sql_database_instance.main.name
}

output "POSTGRES_DB" { value = var.database_name }
output "POSTGRES_USER" { value = var.database_username }
output "POSTGRES_PASSWORD" { value = var.database_password }
output "POSTGRES_HOST" { value = google_sql_database_instance.main.public_ip_address }
output "POSTGRES_PORT" { value = "5432" }

