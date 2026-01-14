from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/seeker/dashboard")
def seeker_dashboard():
    return render_template("seeker.html")

@app.route("/caregiver/dashboard")
def caregiver_dashboard():
    return render_template("caregiver.html")

@app.route("/logout")
def logout():
    return redirect(url_for("login"))

@app.route("/seeker/new")
def seeker_new():
    return render_template("seeker-new.html")

@app.route("/caregiver/new")
def caregiver_new():
    return render_template("caregiver-new.html")

@app.route("/seeker/request")
def seeker_request():
    return render_template("seeker-request.html")

@app.route("/caregiver/profile")
def caregiver_profile():
    return render_template("caregiver-profile.html")

@app.route("/caregiver/newcomer")
def caregiver_newcomer():
    return render_template("caregiver-newbie.html")

if __name__ == "__main__":
    app.run(debug=True)
