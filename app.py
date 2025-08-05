from flask import Flask, render_template, request
from Tax import calculate_tax  # Import tax calculation function
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    tax = None
    effective_tax_rate = None
    income = None

    if request.method == "POST":
        try:
            income = float(request.form["income"])
            tax = calculate_tax(income)
            effective_tax_rate = (tax / income) * 100 if income > 0 else 0
        except ValueError:
            tax = "Invalid Input"
            effective_tax_rate = "N/A"

    return render_template("One.html", tax=tax, effective_tax_rate=effective_tax_rate, income=income)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
