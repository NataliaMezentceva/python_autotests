import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a6bc56a7307e7f2760dc96ba9acf19e6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token'=TOKEN}
TRAINER_ID = 5504

def test_status_code():

response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
assert response.status_code ==200