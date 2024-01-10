from flask import Blueprint, render_template,request
import pandas as pd

search = Blueprint('search', __name__)
movies = pd.read_parquet('df_name.parquet')


def html_block_template(href, name):
    return f'<li><a class="dropdown-item" href="{href}" target="_blank">{name}</a></li>'


@search.route('/search', methods=['GET'])
def query():
    query = request.args.get('query', '')

    results_html = ''

    filtered_movies = movies[movies['name'].str.contains(query, case=False, na=False)]
    

    for d in filtered_movies.values:
        results_html += html_block_template(f'detail?id={d[0]}', d[1])

    return results_html