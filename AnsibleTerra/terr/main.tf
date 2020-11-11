
provider "aws" {
   access_key = "${var.access_key}"
   secret_key = "${var.secret_key}"
   region = "${var.region}"
}

resource "aws_instance" "test_server_master" {
        ami = "${var.ami}"
        instance_type = "${var.instance_type}"
        subnet_id = "${var.subnet_id}"
	private_ip = "172.31.16.10"
        vpc_security_group_ids = [aws_security_group.sg.id]
	key_name = "${var.key_name}"
        tags = {
        Name = "Jenkins-Master"
        }

}

resource "aws_instance" "test_server_slave1" {
        ami = "${var.ami}"
        instance_type = "${var.instance_type}"
        vpc_security_group_ids = [aws_security_group.sg.id]
	key_name = "${var.key_name}"
	subnet_id = "${var.subnet_id}"
        private_ip = "172.31.16.11"
        tags = {
        Name = "Jenkins-Slave-Test"
        }

}

resource "aws_instance" "test_server_slave2" {
        ami = "${var.ami}"
        instance_type = "${var.instance_type}"
        key_name = "${var.key_name}"
        subnet_id = "${var.subnet_id}"
        private_ip = "172.31.16.12"
        vpc_security_group_ids = [aws_security_group.sg.id]
        tags = {
        Name = "Jenkins-Slave-Prod"
        }

}

resource "aws_security_group" "sg" {
          name        = "test"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8989
    to_port     = 8989
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}



output "public_ip_address_master" {
  value = aws_instance.test_server_master.public_ip
}


output "public_ip_address_test" {
  value = aws_instance.test_server_slave1.public_ip
}


output "public_ip_address_prod" {
  value = aws_instance.test_server_slave2.public_ip
}
