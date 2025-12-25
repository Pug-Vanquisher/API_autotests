import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def assert_json_response(r: requests.Response):
    # Базовая проверка того, что ответ похож на JSON
    ct = r.headers.get("Content-Type", "")
    assert "application/json" in ct
    return r.json()


def test_get_user_1():
    r = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT)
    assert r.status_code == 200

    data = assert_json_response(r)

    # Проверка структуры и ключевыъ полей
    assert data.get("id") == 1
    assert "name" in data and isinstance(data["name"], str) and data["name"]
    assert "email" in data and isinstance(data["email"], str) and data["email"]


def test_post_create_user():
    payload = {
        "name": "Mikhail Markov",
        "username": "PugV",
        "email": "Sobsks@mail.ru",
    }

    r = requests.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201

    data = assert_json_response(r)

    # Проверка, что нам вернули id и поля совпадают с отправленными
    assert "id" in data
    assert data.get("name") == payload["name"]
    assert data.get("username") == payload["username"]
    assert data.get("email") == payload["email"]


def test_put_update_user_1():
    payload = {
        "id": 1,
        "name": "Mikhail Markov",
        "username": "PugV2",
        "email": "Sobsks@mail.ru",
    }

    r = requests.put(f"{BASE_URL}/users/1", json=payload, timeout=TIMEOUT)
    assert r.status_code == 200

    data = assert_json_response(r)

    # Проверка, что ответ содержит обновлённые значения
    assert data.get("id") == 1
    assert data.get("name") == payload["name"]
    assert data.get("username") == payload["username"]
    assert data.get("email") == payload["email"]
