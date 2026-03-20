from imports import *

with sqlite3.connect("database.db") as connection:
    cr = connection.cursor()

    cr.execute(
        """
        SELECT name FROM pizza WHERE id IS 1
        """
    )

    rows = cr.fetchall()
    print(rows)
