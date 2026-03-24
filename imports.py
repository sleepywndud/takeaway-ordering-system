from flask import Flask, app, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

with sqlite3.connect("database.db") as connection:
    cr = connection.cursor()
