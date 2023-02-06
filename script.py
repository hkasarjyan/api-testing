import requests
import json
import pytest


def test_google_search():
    url = 'https://www.google.com/search?q=YouTube'
    response = requests.get(url)
    assert "youtube.com" in response.text
    assert response..status_code == 200

def test_post_user():
    url = 'https://crudcrud.com/api/45e13cc8ba9a4c88b71992f31f18763c/users'
    data
    response = requests.post(url, json={"name":"Sparkle Devil","age":4,"colour":"DARK"})
    assert response.status_code == 201

def test_get_user():
    url = 'https://crudcrud.com/api/45e13cc8ba9a4c88b71992f31f18763c/users'
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200


def test_put_user():
    url = 'https://crudcrud.com/api/45e13cc8ba9a4c88b71992f31f18763c/users'
    id = (requests.get(url).json())
    id=id[0]["_id"]
    response = requests.put(url+'/'+id, json={'name':'Angel'})
    assert response.status_code == 200

def test_delete_user():
    url = 'https://crudcrud.com/api/45e13cc8ba9a4c88b71992f31f18763c/users'
    id = (requests.get(url).json())
    id= id[0]["_id"]
    response = requests.delete(url+'/'+id)
    assert response.status_code == 200
