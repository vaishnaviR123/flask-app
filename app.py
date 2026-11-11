from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        ph = float(request.form["ph"])
        turbidity = float(request.form["turbidity"])

        if 6.5 <= ph <= 8.5 and turbidity <= 5:
            result = "Water is Safe to Use"
        else:
            result = "Warning! Water is Contaminated"

    return render_template("index.html", result=result)


if _name_ == "_main_":
    app.run()
