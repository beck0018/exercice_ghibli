from repository import get_all_movie_api, get_one_movie_api
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="view")


def get_all_ghibli_movies(requests: Request):
    ## recuperer la listes des films
    movies = get_all_movie_api()
    movies.sort(key=lambda x: x.release_date)
    return templates.TemplateResponse(
        "movie_view.html", {"request": requests, "movies": movies}
    )


def get_one_ghibli_movies(requests: Request, id_movie):
    ## recuperer un film
    movie = get_one_movie_api(id_movie)
    return templates.TemplateResponse(
        "movie_view.html", {"request": requests, "movies": [movie]}
    )
