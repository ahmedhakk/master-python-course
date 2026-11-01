### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
"""
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to Flask course :)</h1></html>"


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


# Variable rule
@app.route("/success_result/<int:score>")
def success_result(score):
    result = ""
    if score >= 50:
        result = "PASSED"
    else:
        result = "FAILED"

    exp = {"score": score, "result": result}

    return render_template("result1.html", results=exp)


@app.route("/fail/<int:score>")
def fail(score):
    return render_template("result1.html", results=score)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["datascience"])

        total_score = (science + maths + c + data_science) / 4
    else:
        return render_template("get_result.html")
    return redirect(url_for("success_result", score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
