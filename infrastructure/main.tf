terraform {
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

resource "aws_instance" "rag_server" {
  ami           = "ami-0e2c8caa4b6378d8c" 
  instance_type = "t2.micro"              

  tags = {
    Name        = "dev-hybrid-rag-app-01"
    
    Environment = "Development"
    Project     = "Hybrid-RAG"
    ManagedBy   = "Terraform"
  }
}