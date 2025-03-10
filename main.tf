provider "aws" {
	region = "us-east-1"
}

resource "aws_instance" "my_ec2" {
	ami				= "ami-05b10e08d247fb927"
	instance_type	= "t2.micro"
	key_name		= "NewKeyPair"
	tags 			= {
		Name = "TerraformEC2Instance"
	}
}