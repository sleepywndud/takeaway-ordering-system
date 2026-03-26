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
    conn = sqlite3.connect("database.db")  # connect
    cr = conn.cursor()  # cursur setting
    cr.execute("SELECT * FROM pizza")
    data = cr.fetchall()
    conn.close()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

#  -----------------------------------------------------------------
