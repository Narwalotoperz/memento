from flask import Flask, render_template, request, jsonify
import os

# use templates folder one level up (project-level)
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
            static_folder=os.path.join(os.path.dirname(__file__), "..", "static"))
@app.route("/")
def home():
    return render_template("base.html")

@app.route("/form")
def form():
    return render_template("form.html")

notes = {}

@app.route("/calendar")
def calendar():
    return render_template("month_view.html")


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

