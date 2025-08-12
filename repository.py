from fastapi import FastAPI, HTTPException
import requests
from fastapi.responses import JSONResponse
import json
from typing import Any, List, Dict

# call the api
app = FastAPI()

# Constants
URL_API_GHIBLI = "https://ghibliapi.vercel.app/films/"


def get_all_movie_api()-> dict:
    response = requests.get(URL_API_GHIBLI)
    response.raise_for_status()
    return response.json()


def get_one_movie_api(str : id)-> dict:
    response = requests.get(f"{URL_API_GHIBLI}/{id}")
    response.raise_for_status()
    return response.json()
