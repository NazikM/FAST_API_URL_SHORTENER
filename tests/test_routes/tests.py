import pytest


# def test_getting_by_id(client):
#     response = client.get("/api/v1/yTZDuZ")
#     assert response.status_code == 200
#     assert response.json() == "https://fastapi.tiangolo.com/advanced/templates/"


# def test_getting_by_wrong_id():
#     response = client.get("/api/v1/1")
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Url not found!'}
#
#
def test_creating_new(client):
    response = client.post("/api/v1/", json={
        "full": f"https://testdriven.io/1"
    })
    expected = (b'{"full":"https://testdriven.io/1","id":1,"short":"1","click_count":0}', 201)
    assert (response.content, response.status_code) == expected


def test_db_for_empty(client):
    response = client.get("/api/v1/statistics/top_urls/5")
    assert response.content == b'[]'

# def test_creating_old():
#     response = client.post("/api/v1/", json={
#         "full": "https://www.w3resource.com/python-exercises/itertools/index.php"
#     })
#     short = '4S1ISz'
#     assert response.status_code == 201
#     assert response.json()['short'] == short
#
#
# def test_stat_with_adding():
#     response = client.get("/api/v1/statistics/top_urls/100")
#     assert response.status_code == 200
#
#     client.post("/api/v1/", json={
#         "full": "https://testdriven.io/gd"
#     })
#
#     response2 = client.get("/api/v1/statistics/top_urls/100")
#
#     assert response.status_code == 200
#     assert len(response.json()) + 1 == len(response2.json())
#
#
# def test_stat_with_negative_number():
#     response = client.get("/api/v1/statistics/top_urls/-1")
#     assert response.status_code == 400
#
#
# def test_stat_with_not_correct_format():
#     response = client.get("/api/v1/statistics/top_urls/df")
#     assert response.status_code == 422
#     response = client.get("/api/v1/statistics/top_urls/1.0")
#     assert response.status_code == 422
#
#
# def test_stat_for_incrementing_click_count():
#     response = client.get("/api/v1/statistics/top_urls/10")
#     client.get("/" + response.json()[0]['short'])
#     response2 = client.get("/api/v1/statistics/top_urls/10")
#     assert response.json()[0]['click_count'] + 1 == response2.json()[0]['click_count']
