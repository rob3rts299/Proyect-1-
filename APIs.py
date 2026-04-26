#connect to an API using python
#instalacion de requests: "pip install requests"
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:# es codigo de estado de request. el 200 es estado de OK. 400 es estado de ERROR, mas info buscar la bibliografia de codigo de estados.
        pokemon_data = response.json()#transforma la informacion en formato json. 
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")
pokemon_name = "togepi"


pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: 
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
