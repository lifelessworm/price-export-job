import os
import sys
import pandas as pd
import oracledb
from dotenv import load_dotenv

import oracle_client
from paths import root, path

load_dotenv()

def fetch_5098_query():
    try:
        with open(os.path.join(root(), "queries/5098.sql"), "r", encoding="utf-8") as file:
            query = file.read()
            print("Query read successfully!")
            return query
    except Exception as e:
        print(f"Error reading SQL file: {e}")
        sys.exit(1)

def parts_online():
    try:
        sql_path = os.path.join(root(), "queries/5098.sql")
        if not os.path.exists(sql_path):
            print(f"Error: File {sql_path} not found!")
            return
        
        destination_folder = path('PATH_ARS_BASE', 'Ars')
        folder_name = "PFO5098"
        folder_path = os.path.join(destination_folder, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder created at: {folder_path}")

        query = fetch_5098_query()
        print("Fetching data...")

        cursor = oracle_client.conn.cursor()
        cursor.execute(query)
        
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        
        df = pd.DataFrame(rows, columns=columns)

        file_name = f"{folder_name}.csv"
        final_path = os.path.join(folder_path, file_name)

        df.to_csv(final_path, index=False, sep=';', header=False, encoding='utf-8-sig')
        
        if os.path.exists(final_path):
            print(f"FILE LOCATED: {final_path}")
            print(f"File size: {os.path.getsize(final_path)} bytes")
        else:
            print("Python says it saved, but the file isn't there!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()

if __name__ == "__main__":
    parts_online()
