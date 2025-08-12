from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from movies_render import get_all_ghibli_movies, get_one_ghibli_movies
from requests.exceptions import HTTPError
from Httpexception import NotFoundError, InternalServerError

# call the api
app = FastAPI()


# route to get all movies
@app.get("/api/ghibli/films/")
def show_all_movies(request: Request):
    try :
        return get_all_ghibli_movies(request)
    except HTTPError as e:
        if e.response.status_code == 404:
            raise NotFoundError("Pokemon not found")
        raise InternalServerError(str(e))        

# route to get one movies
@app.get("/api/ghibli/films/{id_movie}")
def show_one_movie(request: Request, id_movie: str):
    return get_one_ghibli_movies(request, id_movie)
