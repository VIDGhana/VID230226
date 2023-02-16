from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/general")
def general():
    return render_template("general.html")