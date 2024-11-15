
resource "google_dataproc_cluster" "cluster" {
  name   = "data-cluster"
  region = "us-central1"
}