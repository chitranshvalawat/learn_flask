from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemt import SQLAlchemy

app = Flask(__name__)
app.secret_key = "lakebrains"
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", content=name, r=2, names = ["Chitransh", "Jain", "Khushbu"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"]  =  found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.commit()

        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out!, {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))



@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if  "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))




# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("login.html")


# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"


# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

# @app.route("/test")
# def test():
#     return redirect(url_for("user", name="test!"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)