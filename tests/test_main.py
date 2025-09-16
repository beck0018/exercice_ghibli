from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Test the main FastAPI application and see if the html is correct
def test_show_all_movies():
    response = client.get("/api/ghibli/films/")
    assert response.status_code == 200
    html_content = response.text
    assert "<h1>List of ghibli movies</h1>" in html_content
    assert "<li>" in html_content
    assert (
        "Castle in the Sky (1986)" in html_content
    )  # check known movie
    assert "2006" in html_content  # check known movie release date

#test to get one movie by id and see if the html is correct
def test_show_one_movie():
    movie_id = (
        "2baf70d1-42bb-4437-b551-e5fed5a87abe"  # Example ID for "Castle in the Sky"
    )
    response = client.get(f"/api/ghibli/films/{movie_id}")
    assert response.status_code == 200
    html_content = response.text
    assert "<h1>Details of this movie :" in html_content
    assert "<li>" in html_content
    assert "Castle in the Sky (1986)" in html_content  # check known movie
    assert "1986" in html_content  # check release date
