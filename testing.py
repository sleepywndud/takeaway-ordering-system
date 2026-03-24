from imports import *

with sqlite3.connect("database.db") as connection:
    cr = connection.cursor()
