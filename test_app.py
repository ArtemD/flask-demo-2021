import pytest
from app import app
from create_db import create_db
import os

@pytest.fixture
def client():    
    
    os.environ['DATABASE_URL']='sqlite:///database.db'

    if os.path.exists('database.db') == False:
        create_db()
    
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

def test_form(client):
    result = client.get('/form')
    assert(b'<form action="/submit" method="POST">' in result.data)

def test_index(client):
    result = client.get('/')
    assert(b'<table id="data" class="display" style="width:100%">' in result.data)

def test_submit_redirect(client):
    result = client.get('/submit', follow_redirects=True)
    assert result.request.path == '/form'

def test_submit_add_data(client):
    data = {
        'name': 'Test',
        'address': 'Isokatu 56',
        'postcode': '90100',
        'city': 'Oulu',
        'date': '12.12.2010',
        'type': 'Hard liquor',
        'businessid': '234234-2'
    }
    result = client.post('/submit', data=data)
    assert(b'Data inserted' in result.data)

def test_submit_invalid_data(client):
    data = {
        'type': 'Hard liquor',
        'businessid': '234234-2'
    }
    result = client.post('/submit', data=data)
    assert result.status_code == 400

def test_api_all(client):
    result = client.get('/api/all')
    assert result.content_type == 'application/json'