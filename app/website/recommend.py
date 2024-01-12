from flask import Blueprint, request, render_template
from . import similarity_array, movies_df

recommend = Blueprint("recommend", __name__)


def recommend_movies(movie_name, limit=12):
    try:
        movie_index = movies_df[movies_df["name"] == movie_name].index[0]
        distances = similarity_array[movie_index]
        movies_list = sorted(
            list(enumerate(distances)), reverse=True, key=lambda x: x[1]
        )[1 : limit + 1]

        res = []
        for m in movies_list:
            movie = movies_df.iloc[m[0]]
            res.append(
                {
                    "name": movie["name"],
                    "star": movie["star"],
                    "director": movie["director"],
                    "genre": movie["genre"],
                    "rating": movie["rating"],
                    "year": movie["year"],
                }
            )

        return res

    except:
        return []


@recommend.route("/", methods=["GET"])
def recommend_func():
    movie_name = request.args.get("mname")
    recommendations = recommend_movies(movie_name)
    return render_template(
        "index.html",
        show_recommendations=True,
        res=recommendations,
        movie_name=movie_name,
    )
