from flask import Flask, render_template, request, jsonify
from .config import config
import os
from .database import db

# use templates folder one level up (project-level)
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'), 
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{config['Database']['path']}"

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("calender.html")

@app.route("/form")
def form():
    return render_template("form.html")

notes = {}

@app.route("/save_note", methods=["POST"])
def save_note():
    data = request.json
    notes[data["date"]] = data["note"]
    return {"status": "ok"}


@app.route("/get_note")
def get_note():
    date = request.args.get("date")
    return jsonify({
        "note": notes.get(date, "")
    })

@app.route("/unlock")
def unlock():
    return render_template("unlock.html")

