import sys

from tabulate import tabulate
from connection import create_connection as conn
from pathlib import Path
from sqlite3 import DatabaseError
from prompt_toolkit import prompt

from create_tables import create_tables
from insert_data import insert_sql
from drop_tables import drop_tables
from hello import hello


def queries_by(number_query):
    q_path = Path("sql_scripts")
    q_list = [
        "",
        "query_1.sql",
        "query_2.sql",
        "query_3.sql",
        "query_4.sql",
        "query_5.sql",
        "query_6.sql",
        "query_7.sql",
        "query_8.sql",
        "query_9.sql",
        "query_10.sql",
    ]
    result = None

    with open(q_path.joinpath(q_list[number_query]), "r") as f:
        sql = f.read()

    with conn() as con:
        try:
            cur = con.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            headers = [column[0] for column in cur.description]
            return tabulate(result, headers, tablefmt="pretty")
        except DatabaseError as e:
            print(e)

    return result


def main():
    while True:
        hello()
        try:
            user_input = int(prompt("\nEnter number: ", default=""))

            match user_input:
                case 0:
                    drop_tables()
                    print("\nExit program\n")
                    sys.exit()
                case n if n in range(1, 11):
                    res = queries_by(n)
                    print("\n" + f"{res}")
                case "":
                    print("\nCommand not found!")
                case _:
                    print("\nPlease, enter number from 0 to 10")
        except ValueError:
            print("\n" + "Please, enter number from 0 to 10")
        except DatabaseError as d:
            print("\n" + f"{d}")


if __name__ == "__main__":
    create_tables()
    insert_sql()
    main()
