#!/bin/bash

file=$1
bucket=$2
expires=$3

aws s3 cp "$file" s3://"$bucket"/

aws s3 presign s3://"$bucket"/"$file" --expires-in "$expires"
