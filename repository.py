from fastapi import FastAPI
import requests
from typing import List
from pydantic import BaseModel

# call the api
app = FastAPI()

# Define the Movie model
class Movie(BaseModel):
    id: str
    title: str
    original_title: str
    original_title_romanised: str
    description: str
    director: str
    producer: str
    release_date: str
    running_time: str
    rt_score: str
    people: List[str]
    species: List[str]
    locations: List[str]
    vehicles: List[str]
    url: str


# Constants
URL_API_GHIBLI = "https://ghibliapi.vercel.app/films"

# Functions to interact with the Ghibli API
#  get all movies
def get_all_movie_api() -> List[Movie]:
    response = requests.get(URL_API_GHIBLI)
    response.raise_for_status()
    movies = response.json()
    return [Movie(**movie) for movie in movies]

# get one movie
def get_one_movie_api(id: str) -> Movie:
    response = requests.get(f"{URL_API_GHIBLI}/{id}")
    response.raise_for_status()
    return Movie(**response.json())
