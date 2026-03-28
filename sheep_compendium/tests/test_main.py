from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():

    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    new_sheep_data = {
        "id": 7,
        "name": "Deez",
        "breed": "Nutz",
        "sex": "GOTTEM"
    }

    response = client.post("/sheep/", json=new_sheep_data)

    assert response.status_code == 201
    assert response.json() == new_sheep_data

    get_response = client.get(f"/sheep/{new_sheep_data['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep_data