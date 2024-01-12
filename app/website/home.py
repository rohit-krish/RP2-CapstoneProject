from flask import Blueprint, render_template

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
def home_func():
    return render_template("index.html", show_recommendations=False)
