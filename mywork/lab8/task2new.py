import boto3
import logging
import sys
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_args():
    input_file = sys.argv[1]
    destination = sys.argv[2]
    return input_file, destination

def upload(input_file, destination):
    s3 = boto3.client('s3', region_name='us-east-1')
    try:
        with open(input_file, 'rb') as f:
            s3.put_object(
                Body=f,
                Bucket=destination.split('/')[0],
                Key='/'.join(destination.split('/')[1:])
            )
        logger.info(f"Uploaded {input_file} to {destination}")
    except Exception as e:
        logger.error(f"Failed to upload {input_file}: {e}")

def main():
    input_file, destination = parse_args()
    upload(input_file, destination)

if __name__ == "__main__":
    main()
