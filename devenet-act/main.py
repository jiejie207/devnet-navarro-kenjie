import requests
import random
import json
response1 = requests.get("https://pokeapi.co/api/v2/pokemon/1")
response2= requests.get("https://pokeapi.co/api/v2/pokemon/2")
response3 = requests.get("https://pokeapi.co/api/v2/pokemon/3")
response4 = requests.get("https://pokeapi.co/api/v2/pokemon/4")
response5 = requests.get("https://pokeapi.co/api/v2/pokemon/5")

##pokemon = ["charizard", "blastoise", "metapod", "bulbasaur", "charmander"]


print(response.status_code)
pokemon_data1 = response1.json()
name = pokemon_data1.get("name")
height = pokemon_data1.get("height")
weight = pokemon_data1.get("weight")

print(name)

pokemon_data2 = response2.json()
name = pokemon_data2.get("name")
height = pokemon_data2.get("height")
weight = pokemon_data2.get("weight")

print(name)

pokemon_data3 = response3.json()
name = pokemon_data3.get("name")
height = pokemon_data3.get("height")
weight = pokemon_data3.get("weight")

print(name)

pokemon_data4 = response4.json()
name = pokemon_data4.get("name")
height = pokemon_data4.get("height")
weight = pokemon_data4.get("weight")

print(name)

pokemon_data5 = response5.json()
name = pokemon_data5.get("name")
height = pokemon_data5.get("height")
weight = pokemon_data5.get("weight")

print(name)

##for name in pokemon_data:
   ## if name == "name":
       ## print(name)