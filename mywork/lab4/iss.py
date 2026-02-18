#!/usr/bin/env python3
"""
ETL Lab 4: Track ISS Location Over Time
Automatically fetches ISS location, transforms it, and appends to CSV.
"""

import os
import sys
import logging
import requests
import pandas as pd

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"

def parse_args():
    try:
        csv_file = sys.argv[1]
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <output_csv_file>")
        sys.exit(1)
    return csv_file

def extract(url):
    logging.info(f"Fetching data from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info("Extract successful")
        return data
    except requests.RequestException as e:
        logging.error(f"Extract failed: {e}")
        return None

def transform(data):
    if data is None:
        logging.warning("No data to transform")
        return None
    try:
        timestamp = pd.to_datetime(data['timestamp'], unit='s')
        position = data['iss_position']
        df = pd.DataFrame([{
            'timestamp': timestamp,
            'latitude': position['latitude'],
            'longitude': position['longitude']
        }])
        logging.info("Transform successful")
        return df
    except KeyError as e:
        logging.error(f"Transform failed: {e}")
        return None

def load(df, csv_file):
    if df is None:
        logging.warning("No data to load")
        return
    try:
        if os.path.exists(csv_file):
            df.to_csv(csv_file, mode='a', index=False, header=False)
            logging.info(f"Appended to CSV {csv_file}")
        else:
            df.to_csv(csv_file, index=False)
            logging.info(f"Created CSV {csv_file}")
    except Exception as e:
        logging.error(f"Load failed: {e}")

def main():
    logging.info("ISS ETL PIPELINE STARTING")
    csv_file = parse_args()
    data = extract(URL)
    df = transform(data)
    load(df, csv_file)
    if df is not None:
        logging.info(f"Processed {len(df)} record(s)")

if __name__ == "__main__":
    main()
