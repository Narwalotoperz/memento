from flask import Flask, render_template
import os

# use templates folder one level up (project-level)
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"))

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/calender_month")
def calender_month_view():
    return render_template("month_view.html")

@app.route("/notes_and_tasks")
def notes_and_tasks_view():
    return render_template("notes_and_tasks.html")

@app.route("/unlock")
def unlock():
    return render_template("unlock.html")

