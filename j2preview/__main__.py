from flask import Flask, render_template, request
import os, yaml
from .AnsibleParser import renderTemplate

app = Flask(__name__)

print()


@app.route("/", methods=("GET", "POST"))
@app.route("/index", methods=("GET", "POST"))
def index():
    JinjaOutput = ""
    if request.method == "POST":
        YamlInput = yaml.safe_load(request.form["YamlInput"])
        JinjaInput = request.form["JinjaInput"]

        JinjaOutput = renderTemplate(YamlInput, JinjaInput)
        print(JinjaOutput)

    return render_template("index.html", request=request, JinjaOutput=JinjaOutput)


if __name__ == "__main__":
    app.run(debug=True)
