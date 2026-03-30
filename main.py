"""
Takeaway ordering system for Domino's
Created by: James Park
Project Started on 19.03.2026
"""

#  -----------------------------------------------------------------

from imports import *

app = Flask(__name__)
voucher_status = "Not Applied"


@app.route("/", methods=["GET", "POST"])
def main():
    global voucher_status
    conn = sqlite3.connect("database.db")  # connect
    cr = conn.cursor()  # cursor setting

    cr.execute("SELECT * FROM pizza")
    data = cr.fetchall()

    if request.method == "POST":
        if voucher_status == "Voucher Applied":
            voucher_status = "Not Applied"
            voucher_button_status = "Apply Voucher"
        else:
            voucher_status = "Voucher Applied"
            voucher_button_status = "Unapply Voucher"

    return render_template(
        "index.html",
        data=data,
        voucher_status=voucher_status,
        voucher_button_status=voucher_button_status,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)

#  -----------------------------------------------------------------
