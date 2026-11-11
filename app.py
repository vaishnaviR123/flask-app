import os
from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template(
        "index.html",
        message="Hello from the cloud!"
    )

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
