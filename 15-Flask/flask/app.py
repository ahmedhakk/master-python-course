from flask import Flask

"""
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
"""

###WSGI Application
app = Flask(__name__)


# create a basic route.
@app.route("/")
def welcome():
    return "Welcome to Flask course :)"


@app.route("/index")
def index():
    return "Welcome to index page :)"


if __name__ == "__main__":
    app.run(debug=True)
