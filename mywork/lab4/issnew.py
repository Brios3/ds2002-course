import os
import sys
import logging
import requests
import pandas as pd
import mysql.connector

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"

DB_HOST = "ds2002.cgls84scuy1e.us-east-1.rds.amazonaws.com"
DB_USER = "ds2002"
DB_NAME = "iss"
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")

REPORTER_ID = "yourcomputingid"
REPORTER_NAME = "Your Name"


def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


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
            'longitude': position['longitude'],
            'message': data['message']
        }])
        logging.info("Transform successful")
        return df
    except KeyError as e:
        logging.error(f"Transform failed: {e}")
        return None


def register_reporter(table, reporter_id, reporter_name):

    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor()

        query = f"SELECT reporter_id FROM {table} WHERE reporter_id = %s"
        cursor.execute(query, (reporter_id,))
        result = cursor.fetchone()

        if result is None:
            insert_query = f"""
            INSERT INTO {table} (reporter_id, reporter_name)
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (reporter_id, reporter_name))
            db.commit()
            logging.info("Reporter registered")
        else:
            logging.info("Reporter already exists")

    except Exception as e:
        logging.error(f"Reporter registration failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def load(df):

    if df is None:
        logging.warning("No data to load")
        return

    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor()

        row = df.iloc[0]

        insert_query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(insert_query, (
            row['message'],
            row['latitude'],
            row['longitude'],
            row['timestamp'],
            REPORTER_ID
        ))

        db.commit()

        logging.info("Location inserted into database")

    except Exception as e:
        logging.error(f"Load failed: {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def main():

    register_reporter("reporters", REPORTER_ID, REPORTER_NAME)

    data = extract(URL)
    df = transform(data)

    load(df)


if __name__ == "__main__":
    main()
