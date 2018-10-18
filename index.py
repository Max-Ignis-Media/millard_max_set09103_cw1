from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/lrseries")
def lrseries():
        return render_template("lrseries.html")

@app.route("/oneten")
def oneten():
        return render_template("oneten.html")

@app.route("/defender")
def defender():
        return render_template("defender.html")

