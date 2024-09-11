from flask import Flask, render_template, request
import os

app = Flask(__name__)

print()


@app.route("/", methods=("GET", "POST"))
@app.route("/index", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        print(request.form)

    return render_template("index.html", request=request)


if __name__ == "__main__":
    app.run(debug=True)
