from repository import Movie, get_all_movie_api, get_one_movie_api

# Test get_all_movie_api and get_one_movie_api functions
# test to get all movies from the API
def test_get_all_movie_api():
    movies = get_all_movie_api()
    assert isinstance(movies, list)
    assert len(movies) > 0
    assert all(isinstance(movie, Movie) for movie in movies)

# test to get one movie from the API
def test_get_one_movie_api():
    movie_id = "2baf70d1-42bb-4437-b551-e5fed5a87abe"  # Example ID
    movie = get_one_movie_api(movie_id)
    assert isinstance(movie, Movie)
    assert movie.id == movie_id
