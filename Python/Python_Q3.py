"""
Question 3: -
Write a program, which would download the data from the provided link, and then read the data and convert
that into properly structured data and return it in Excel format.

Note - Write comments wherever necessary explaining the code written.

Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json

Data Attributes - id: Identification Number - int num: Number of the

● Pokémon in the official Pokédex - int name: Pokémon name -

● string img: URL to an image of this Pokémon - string type:

● Pokémon type -string height: Pokémon height - float

● weight: Pokémon weight - float candy: type of candy used to evolve Pokémon or
given

● when transferred - string candy_count: the amount of candies required to evolve
- int

● egg: Number of kilometers to travel to hatch the egg - float spawn_chance:

● Percentage of spawn chance (NEW) - float avg_spawns: Number of this
pokemon on 10.000 spawns (NEW) - int

● spawn_time: Spawns most active at the time on this field. Spawn times are the same for all
time zones and are expressed in local time. (NEW) - “minutes: seconds” multipliers:
Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int
weakness: Types of

● Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of
successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous
evolutions of Pokémon - - list of dict
"""

#Ans:

import pandas as pd
import requests

# Download the data from the provided link
data_url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
response = requests.get(data_url)
data = response.json()

# Create empty lists to store the extracted attributes
ids = []
nums = []
names = []
imgs = []
types = []
heights = []
weights = []
candies = []
candy_counts = []
eggs = []
spawn_chances = []
avg_spawns = []
spawn_times = []
multipliers = []
weaknesses = []
next_evolutions = []
prev_evolutions = []

# Extract the attributes from the data
for entry in data['pokemon']:
    ids.append(entry['id'])
    nums.append(entry['num'])
    names.append(entry['name'])
    imgs.append(entry['img'])
    types.append(', '.join(entry['type']))
    heights.append(entry['height'])
    weights.append(entry['weight'])
    candies.append(entry.get('candy', ''))
    candy_counts.append(entry.get('candy_count', ''))
    eggs.append(entry.get('egg', ''))
    spawn_chances.append(entry.get('spawn_chance', ''))
    avg_spawns.append(entry.get('avg_spawns', ''))
    spawn_times.append(entry.get('spawn_time', ''))
    multipliers.append(entry.get('multipliers', ''))
    weaknesses.append(', '.join(entry.get('weaknesses', [])))

    next_evolutions.append(', '.join([evolution['num'] + '-' + evolution['name'] for evolution in entry.get('next_evolution', [])]))
    prev_evolutions.append(', '.join([evolution['num'] + '-' + evolution['name'] for evolution in entry.get('prev_evolution', [])]))

# Create a DataFrame to store the extracted data
df = pd.DataFrame({
    'ID': ids,
    'Number': nums,
    'Name': names,
    'Image': imgs,
    'Type': types,
    'Height': heights,
    'Weight': weights,
    'Candy': candies,
    'Candy Count': candy_counts,
    'Egg': eggs,
    'Spawn Chance': spawn_chances,
    'Average Spawns': avg_spawns,
    'Spawn Time': spawn_times,
    'Multipliers': multipliers,
    'Weaknesses': weaknesses,
    'Next Evolution': next_evolutions,
    'Previous Evolution': prev_evolutions
})

# Export the DataFrame to an Excel file
excel_file = 'pokemon_data.xlsx'
df.to_excel(excel_file, index=False)
print(f"Data has been exported to '{excel_file}'.")



