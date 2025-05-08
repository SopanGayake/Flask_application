from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index_page():
    # Render the index.html template  9999
    return render_template("index.html")

@main.route("/<path:subpath>")
def handle_subpath(subpath):
    # Render the student_form.html template
    return render_template("student_form.html", subpath=subpath)

