This Terraform configuration provisions version-controlled, secure cloud storage buckets for your MLflow model registry artifacts

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "mlops_artifacts" {
  bucket = "aobakwe-mlops-model-registry-artifacts"

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
    Owner       = "Aobakwe Mokgothu-Kugombo"
  }
}

resource "aws_s3_bucket_versioning" "artifact_versioning" {
  bucket = aws_s3_bucket.mlops_artifacts.id
  versioning_configuration {
    status = "Enabled"
  }
}
