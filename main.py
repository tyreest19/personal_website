from flask import Flask
from flask import render_template


app = Flask(__name__,template_folder='templates',static_url_path = '/static')
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/resume")
def resume():
    return render_template("resume.html",)

@app.route("/projects")
def projects():
    return render_template("projects.html")
@app.route("/experience")
def experience():
    return render_template("experience.html")

if __name__ == "__main__":
    app.run(debug=True)