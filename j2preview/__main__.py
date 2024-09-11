from flask import Flask, render_template, request
import os, yaml
from .AnsibleParser import renderTemplate

app = Flask(__name__)

print()


@app.route("/", methods=("GET", "POST"))
@app.route("/index", methods=("GET", "POST"))
def index():
    JinjaOutput = ""
    styleClass = "noerror"
    if request.method == "POST":
        Error = False
        try:
            YamlInput = yaml.safe_load(request.form["YamlInput"])
            JinjaInput = request.form["JinjaInput"]

            JinjaOutput, Error = renderTemplate(YamlInput, JinjaInput)
        except Exception as err:
            Error = True
            JinjaOutput = err
        if Error == True:
            styleClass = "error"
        else:
            styleClass = "success"
    return render_template(
        "index.html", request=request, JinjaOutput=JinjaOutput, styleClass=styleClass
    )


if __name__ == "__main__":
    app.run(debug=True)
