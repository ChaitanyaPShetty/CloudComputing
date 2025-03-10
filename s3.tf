provider "aws" {
	region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "chais3bucketterraform"  # Replace with a globally unique name
}

resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.my_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
