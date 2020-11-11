variable access_key {
  description = "Enter access key"
}

variable secret_key {
  description = "Enter secret key"
}

variable key_name {
  description = "Enter key name"
}


variable region {
  description = "Region"
  default     = "europe-west1"
}


variable "ami" {
  description = "ID of AMI to use for the instance"
  type        = string
}


variable "subnet_id" {
  description = "The VPC Subnet ID to launch in"
  type        = string
}


variable "instance_type" {
  description = "Enter instance type"
}
