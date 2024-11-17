set -e
set -o pipefail
set -u

echo "############# Copy data from local to GCS bucket"

gsutil cp -r data/ gs://co2-data-bucket/