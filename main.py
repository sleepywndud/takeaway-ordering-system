"""
Takeaway ordering system for Domino's
Created by: James Park
Project Started on 19.03.2026
"""

#  -----------------------------------------------------------------

from imports import *

app = Flask(__name__)


@app.route("/")
def main():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM pizza")
    pizzas = cur.fetchall()
    con.close()
    return render_template("index.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

#  -----------------------------------------------------------------
