import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a6bc56a7307e7f2760dc96ba9acf19e6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token'=TOKEN}

body_post_pokemons = {
    "name": "Rik",
    "photo_id": 45
}

body_put_pokemons = {
    "pokemon_id": "46444",
    "name": "Fil",
    "photo_id": 45
}

body_post_pokeball = {
    "pokemon_id": "75360"
}

response_post_pokemons  = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_post_pokemons )
print(response_post_pokemons.text)

pokemon_id = response_post_pokemons.json()['id']

response_put_pokemons  = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_pokemons )
print(response_put_pokemons.text)

response_post_pokeball  = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_postpokemons )
print(response_post_pokeball.text)

