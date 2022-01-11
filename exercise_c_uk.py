united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

united_kingdom [0]["capital"] = "Cardiff"
print(united_kingdom)

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).

northern_island = {
  "name": "Northern Island",
  "population": 1811000,
  "capital": "Belfast"
}

united_kingdom.append(northern_island)
print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.

for nation in united_kingdom:
  print(nation.get("name"))

# 4. Use a loop to find the total population of the UK.

total_population = 0

for nation in united_kingdom:
   total_population += nation.get("population")

print(total_population)
