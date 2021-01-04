from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

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
    return render_template()

@app.route("<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


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
    app.run(debug=True)