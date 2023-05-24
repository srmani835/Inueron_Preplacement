'''
Question-6 
Using the data from Question 3, write code to analyze the data and answer the following questions 

Note:-
1. Draw plots to demonstrate the analysis for the following questions for better visualizations.
2. Write code comments wherever required for code understanding

Insights to be drawn -

* Get all Pokemons whose spawn rate is less than 5%
* Get all Pokemons that have less than 4 weaknesses
* Get all Pokemons that have no multipliers at all
* Get all Pokemons that do not have more than 2 evolutions
* Get all Pokemons whose spawn time is less than 300 seconds.

Note - spawn time format is "05:32”, so assume “minute: second” format and perform the analysis.

* Get all Pokemon who have more than two types of capabilities

'''


# Ans:

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel('pokemon_data.xlsx')



# Get all Pokemons whose spawn rate is less than 5%
spawn_rate = df[df['Spawn Chance'] < 5]

# Plot a bar chart for spawn rate
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(spawn_rate['Name'], spawn_rate['Spawn Chance'])
ax.set_xticklabels(spawn_rate['Name'], rotation=90)
ax.set_xlabel('Pokemon Name')
ax.set_ylabel('Spawn Rate')
ax.set_title('Pokemon Spawn Rate')



# Get all Pokemons that have less than 4 weaknesses
weaknesses = df[df['Number of Weaknesses'] < 4]

# Plot a line chart for weaknesses
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(weaknesses['Name'], weaknesses['Number of Weaknesses'])
ax.set_xticklabels(weaknesses['Name'], rotation=90)
ax.set_xlabel('Pokemon Name')
ax.set_ylabel('Number of Weaknesses')
ax.set_title('Pokemon Weaknesses')



# Get all Pokemons that have no multipliers at all
multipliers = df[df['Multipliers'].isnull()]

# Plot a scatter plot for multipliers
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(multipliers['Attack'], multipliers['Defense'])
ax.set_xlabel('Attack')
ax.set_ylabel('Defense')
ax.set_title('Pokemon Multipliers')



# Get all Pokemons that do not have more than 2 evolutions
evolutions = df[df['Number of Evolutions'] <= 2]

# Plot a pie chart for evolutions
fig, ax = plt.subplots(figsize=(10, 6))
ax.pie(evolutions.groupby(['Legendary'])['Name'].count(), labels=['False', 'True'], autopct='%1.1f%%')
ax.set_title('Pokemon Evolutions')



# Get all Pokemons whose spawn time is less than 300 seconds.
spawn_time = df[df['Spawn Time'] < '00:05:00']

# Plot a histogram for spawn time
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(spawn_time['Spawn Time'])
ax.set_xlabel('Spawn Time')
ax.set_ylabel('Frequency')
ax.set_title('Pokemon Spawn Time')



# Get all Pokemon who have more than two types of capabilities
types = df[df['Type'].str.contains(',')]

# Plot a stacked bar chart for types
fig, ax = plt.subplots(figsize=(10, 6))
types.groupby(['Type']).size().unstack().plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Pokemon Type')
ax.set_ylabel('Count')
ax.set_title('Pokemon Types')

# Show the plots
plt.show()
