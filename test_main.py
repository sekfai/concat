from urllib.parse import urlencode

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# test /concatenate endpoints
def test_concatenate():
    response = client.get("/concatenate?str1=abc&str2=xyz")
    assert response.status_code == 200
    assert response.json() == "abcxyz"

def test_concatenate_empty_strings():
    response = client.get("/concatenate?str1=&str2=")
    assert response.status_code == 200
    assert response.json() == ""

def test_concatenate_special_characters():
    params = {'str1': 'abc', 'str2': 'xyz!@#$'}
    response = client.get("/concatenate?"+urlencode(params))
    assert response.status_code == 200
    assert response.json() == params['str1'] + params['str2']

def test_concatenate_long_strings():
    str1 = 'a' * 100
    str2 = 'b' * 100
    response = client.get(f"/concatenate?str1={str1}&str2={str2}")
    assert response.status_code == 200
    assert response.json() == str1 + str2

# repeat above tests on the /concatenate_fast endpoints
def test_concatenate_fast():
    response = client.get("/concatenate_fast?str1=abc&str2=xyz")
    assert response.status_code == 200
    assert response.json() == "abcxyz"

def test_concatenate_fast_empty_strings():
    response = client.get("/concatenate_fast?str1=&str2=")
    assert response.status_code == 200
    assert response.json() == ""

def test_concatenate_fast_special_characters():
    params = {'str1': 'abc', 'str2': 'xyz!@#$'}
    response = client.get("/concatenate_fast?"+urlencode(params))
    assert response.status_code == 200
    assert response.json() == params['str1'] + params['str2']

def test_concatenate_fast_long_strings():
    str1 = 'a' * 100
    str2 = 'b' * 100
    response = client.get(f"/concatenate_fast?str1={str1}&str2={str2}")
    assert response.status_code == 200
    assert response.json() == str1 + str2
