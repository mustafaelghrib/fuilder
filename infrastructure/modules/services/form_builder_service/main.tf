
variable "database_instance_name" { type = string }
variable "database_name" { type = string }
variable "database_username" { type = string }
variable "database_password" { type = string }

module "sql_database" {
  source                 = "../../gcp/sql_database"

  database_instance_name = var.database_instance_name
  database_version       = "POSTGRES_14"
  database_tier          = "db-f1-micro"
  database_name          = var.database_name
  database_username      = var.database_username
  database_password      = var.database_password

}

output "sql_database" {
  value     = module.sql_database
  sensitive = true
}

variable "storage_name" { type = string }

module "storage_bucket" {
  source           = "../../gcp/storage_bucket"

  storage_name     = var.storage_name
  storage_location = "US-EAST1"

}

output "storage_bucket" {
  value     = module.storage_bucket
  sensitive = true
}
