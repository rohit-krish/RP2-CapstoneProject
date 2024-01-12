from flask import Blueprint, request
from . import movies_df

search = Blueprint("search", __name__)


def html_dropdown_item_template(href, title):
    return (
        f'<li><a class="dropdown-item" href="{href}">{title}</a></li>'
    )


@search.route("/", methods=["GET"])
def search_func():
    query = request.args.get("query")

    filtered_movies = movies_df[
        movies_df["name"].str.contains(query, case=False, na=False, regex=False)
    ]
    html_result = ""

    for m in filtered_movies.values:
        html_result += html_dropdown_item_template("/recommend/?mname="+m[0], m[0])

    return html_result
