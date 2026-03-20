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
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)

#  -----------------------------------------------------------------
