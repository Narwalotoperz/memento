from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from .config import config
import os
from .database import db
from .form import ProfileForm
from .database import User

# use templates folder one level up (project-level)
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'), 
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{config['Database']['path']}"
app.config["SECRET_KEY"] = "dev-secret-key"

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("calender.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    userForm  = ProfileForm()
    return render_template("form.html", userForm=userForm)

@app.route("/submit-profile", methods=["GET", "POST"])
def submit_profile():
    userForm  = ProfileForm()
    existing = User.query.filter_by(name=userForm.name.data).first()
    if existing:
            flash("User already exists", "danger")
    else:        
        if userForm.validate_on_submit():
            
            user = User(
                name=userForm.name.data,
                gender=userForm.gender.data,
                age=userForm.age.data,
                social_class=userForm.social_class.data,
                country=userForm.country.data
            )
            
            db.session.add(user)
            db.session.commit()
            flash("User created successfully", "success")
            return redirect(url_for("home"))
    return render_template("form.html", userForm=userForm)

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

