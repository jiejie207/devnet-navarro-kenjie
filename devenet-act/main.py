import requests
import random

response1 = requests.get("https://pokeapi.co/api/v2/pokemon/1")
response2 = requests.get("https://pokeapi.co/api/v2/pokemon/2")
response3 = requests.get("https://pokeapi.co/api/v2/pokemon/3")
response4 = requests.get("https://pokeapi.co/api/v2/pokemon/4")
response5 = requests.get("https://pokeapi.co/api/v2/pokemon/5")

print(response1.status_code)

pokemon_data1 = response1.json()
pokemon_data2 = response2.json()
pokemon_data3 = response3.json()
pokemon_data4 = response4.json()
pokemon_data5 = response5.json()

name1 = pokemon_data1.get("name")
name2 = pokemon_data2.get("name")
name3 = pokemon_data3.get("name")
name4 = pokemon_data4.get("name")
name5 = pokemon_data5.get("name")

height1 = pokemon_data1.get("height")
weight1 = pokemon_data1.get("weight")

height2 = pokemon_data2.get("height")
weight2 = pokemon_data2.get("weight")

height3 = pokemon_data3.get("height")
weight3 = pokemon_data3.get("weight")

height4 = pokemon_data4.get("height")
weight4 = pokemon_data4.get("weight")

height5 = pokemon_data5.get("height")
weight5 = pokemon_data5.get("weight")

abilities1 = []
for item in pokemon_data1.get("abilities", []):
    abilities1.append(item["ability"]["name"])

abilities2 = []
for item in pokemon_data2.get("abilities", []):
    abilities2.append(item["ability"]["name"])

abilities3 = []
for item in pokemon_data3.get("abilities", []):
    abilities3.append(item["ability"]["name"])

abilities4 = []
for item in pokemon_data4.get("abilities", []):
    abilities4.append(item["ability"]["name"])

abilities5 = []
for item in pokemon_data5.get("abilities", []):
    abilities5.append(item["ability"]["name"])

pokemon_names = [name1, name2, name3, name4, name5]
pokemon_data = [
    pokemon_data1,
    pokemon_data2,
    pokemon_data3,
    pokemon_data4,
    pokemon_data5
]

chosen = random.randint(0, 4)
answer = pokemon_names[chosen]
data = pokemon_data[chosen]

print("Guess the pokemon")

print("Height:", data.get("height"))
print("Weight:", data.get("weight"))

abilities = []
for item in data.get("abilities", []):
    abilities.append(item["ability"]["name"])

print("Abilities:", abilities)

for i in range(3):
    guess = input("\nEnter your guess: ").lower()

    if guess == answer:
        print("Tama ka ya")
        break
    else:
        print("Mali ka ya")

else:
    print("Talo kana ya", answer)