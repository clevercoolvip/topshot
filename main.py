from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feedbacks.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)

class Feedbacks(db.Model):
    ID = db.Column("User_ID", db.INTEGER, primary_key=True)
    name = db.Column("Name", db.String(100))
    phone = db.Column("Phone", db.String(10))
    email = db.Column("EMail", db.String(100))
    message = db.Column("Message", db.String(1500))

    def __init__(self, name, phone, email, message):
        self.name = name
        self.phone = phone
        self.email = email
        self.message = message


db.create_all()

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"{name} | {phone} | {email} | {message}")
        feedback = Feedbacks(name, phone, email, message)
        db.session.add(feedback)
        db.session.commit()
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method=="POST":
        email = request.form.get("email_contact")
        message = request.form.get("message_contact")
        with open("contact_data/data.txt", "a+") as file:
            file.write(f"'{email}', '{message}'\n")

    return render_template("contact.html")


@app.route("/test1")
def test1():
    return render_template("test1.html")

if __name__=="__main__":
    app.run(debug=True)