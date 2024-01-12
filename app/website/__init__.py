from flask import Flask
from pandas import read_parquet

# reading the saved data
movies_df = read_parquet("website/static/df_n-s-d-g-r-y.parquet")
similarity_array = read_parquet("website/static/df_similarity_bow.parquet").values


def create_app():
    app = Flask(__name__)

    from .home import home
    from .search import search
    from .recommend import recommend

    app.register_blueprint(home, prefix="/")
    app.register_blueprint(search, url_prefix="/search")
    app.register_blueprint(recommend, url_prefix="/recommend")

    return app
