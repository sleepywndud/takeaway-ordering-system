from flask import Flask, app, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
