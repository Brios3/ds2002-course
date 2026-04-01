#!/bin/bash
AMI=ami-042e8287309f5df03
INSTANCE_TYPE=t2.nano
INSTANCE_NAME=ds2002-cwb3ud
KEY_NAME=key-ec2-new
SECURITY_GROUP_ID=sg-04f4505ecb775b95b
SUBNET_ID=subnet-085a38474f2e3b60c

aws ec2 run-instances \
  --image-id $AMI \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-group-ids $SECURITY_GROUP_ID \
  --subnet-id $SUBNET_ID \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$INSTANCE_NAME}]"
