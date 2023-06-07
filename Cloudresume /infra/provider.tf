terraform {
  required_providers {
    aws = {
      version = ">= 4.9.0"
      source  = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "johnathan"
  region  = "us-east-1"
}

data "aws_shared_credentials" "example" {
  profile = "johnathan"
}

resource "null_resource" "write_credentials_file" {
  provisioner "local-exec" {
    command = <<-EOT
      mkdir -p /Users/johnathanhorner/.aws/
      echo -e "[johnathan]\naws_access_key_id = ${data.aws_shared_credentials.example.access_key}\naws_secret_access_key = ${data.aws_shared_credentials.example.secret_key}" > /Users/johnathanhorner/.aws/credentials
    EOT
  }
}
