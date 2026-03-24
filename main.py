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
    conn = sqlite3.connect("database.db")
    cr = conn.cursor()
    cr.execute("SELECT * FROM pizza")
    pizzas = cr.fetchall()
    conn.close()
    return render_template("index.html", pizzas=pizzas)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

#  -----------------------------------------------------------------
