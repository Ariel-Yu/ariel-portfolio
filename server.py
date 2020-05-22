import csv

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# Start of the application
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<string:name>')
def page(name: str = "index"):
    return render_template(name + ".html")


def write_to_database(data: dict) -> None:
    with open("database.csv", mode="a") as database:
        csv.writer(database, delimiter=",").writerow(data.values())


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        write_to_database(request.form.to_dict())
        return redirect("/thank_you")
    else:
        return redirect("/sorry")
