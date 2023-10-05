from connection import create_connection
from sqlite3 import DatabaseError
from pathlib import Path

sql_path = Path("sql_scripts")


def create_tables():
    with open(f"{sql_path.joinpath('create_tables.sql')}", "r") as file:
        sql_script = file.read()

    conn = None
    with create_connection() as conn:
        try:
            if conn is not None:
                cur = conn.cursor()
                cur.executescript(sql_script)
            else:
                print("Connection error")
        except DatabaseError as d:
            print(d)


if __name__ == "__main__":
    create_tables()
