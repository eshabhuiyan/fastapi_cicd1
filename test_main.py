from fastapi.testclient import TestClient
from main import api   

client = TestClient(api)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

def test_add_book():
    book = {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python from scratch",
        "isAvailable": True
    }
    response = client.post("/book", json=book)
    assert response.status_code == 200
    assert any(b["id"] == 1 for b in response.json())

def test_get_books():
    response = client.get("/book")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_book():
    updated_book = {
        "id": 1,
        "name": "Python Advanced",
        "description": "Learn advanced Python",
        "isAvailable": False
    }
    response = client.put("/book/1", json=updated_book)
    assert response.status_code == 200
    assert response.json()["name"] == "Python Advanced"

def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
