from flask import Flask, render_template, json
app = Flask(__name__)

@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/lrseries")
def lrseries():
        return render_template("lrseries.html")

@app.route("/lrseriesEO")
def lrseriesEO():
        return render_template("lrseriesEO.html")

@app.route("/lrseriesET")
def lrseriesET():
        return render_template("lrseriesET.html")

@app.route("/lrseriesEH")
def lrseriesEH():
        return render_template("lrseriesEH.html")

@app.route("/oneten")
def oneten():
        return render_template("oneten.html")

@app.route("/onetenEO")
def onetenEO():
        return render_template("onetenEO.html")

@app.route("/onetenET")
def onetenET():
        return render_template("onetenET.html")

@app.route("/petrol")
def petrol():
        return render_template("petrol.html")

@app.route("/diesel")
def diesel():
	return render_template("diesel.html")

@app.route("/defender")
def defender():
        return render_template("defender.html")

@app.route("/defenderEO")
def defenderEO():
        return render_template("defenderEO.html")

@app.route("/defenderET")
def defenderET():
        return render_template("defenderET.html")

@app.route("/defenderEH")
def defenderEH():
        return render_template("defenderEH.html")

@app.route("/onetenEH")
def onetenEH():
	return render_template("onetenEH.html")
@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html"), 404
