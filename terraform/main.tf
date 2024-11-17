terraform {
  required_providers {
    google = {
        source = "hashicorp/google"
    }
  }
}

provider "google" {
  project = var.project_id
  region = var.region
  zone = var.zone
}


resource "google_storage_bucket" "co2" {
 name          = "co2-data-bucket"
 location      = "US"
 storage_class = "STANDARD"

 uniform_bucket_level_access = true
}


resource "google_bigquery_dataset" "datasets" {
  project       = var.project_id
  dataset_id    = "co2_dataset" 
  friendly_name = "DataSet that contains the Co2 data "
  description   = "DataSet that contains the annual Co2 emissions data for all countries "
  location      = "US"
}