import requests


def test_http():
    s = requests.get("https://selectel.ru")
    assert s.status_code == 200