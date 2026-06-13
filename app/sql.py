import sqlite3
import pandas as pd
from pathlib import Path


DB_PATH = Path(__file__).parent / "db.sqlite"


def run_query(query):
   

    with sqlite3.connect(DB_PATH) as conn:
        

        df = pd.read_sql_query(query, conn)
        return df


if __name__ == "__main__":
    query = "SELECT * FROM product WHERE brand LIKE '%nike%'"
    df = run_query(query)
    print(df)