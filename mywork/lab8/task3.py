import boto3
import argparse
import logging
import os
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", help="Folder containing results CSV files")
    parser.add_argument("destination", help="S3 bucket/prefix to upload to")
    args = parser.parse_args()
    return args.input_folder, args.destination

def upload(input_folder, destination):
    try:
        s3 = boto3.client("s3", region_name="us-east-1")
        bucket_name, *prefix_parts = destination.split("/", 1)
        prefix = prefix_parts[0] if prefix_parts else ""
        for fname in os.listdir(input_folder):
            if fname.startswith("results") and fname.endswith(".csv"):
                local_path = os.path.join(input_folder, fname)
                key = f"{prefix}/{fname}" if prefix else fname
                s3.upload_file(local_path, bucket_name, key)
                logger.info(f"Uploaded {fname} to {bucket_name}/{key}")
    except Exception as e:
        logger.error(f"Failed to upload files: {e}")

def main():
    input_folder, destination = parse_args()
    upload(input_folder, destination)
    logger.info("Task 3 upload complete.")

if __name__ == "__main__":
    main()

