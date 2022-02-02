# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damages):
  updated_damages = []
  for record in damages:
    if record[-1] in conversion:
      updated_damages.append(float(record[:-1]) * conversion[record[-1]])
    else:
      updated_damages.append(record)
  return updated_damages
 
# test function by updating damages
print(damages)
print("--------------")
updated_damages = update_damages(damages)
print(updated_damages)
# 2 
# Create a Table
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  dictionary = {}
  for index in range(len(names)):
    dictionary[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages[index], "Deaths": deaths[index] }
  return dictionary


# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print("--------------")
print(hurricanes["Irma"])



# 3
# Organizing by Year
def organize_by_year(hurricanes):
  by_year = {}
  for current_hurricane in hurricanes:
    current_year = hurricanes[current_hurricane]["Year"]
    if current_year not in by_year:
      by_year[current_year] = [hurricanes[current_hurricane]]
    else:
      by_year[current_year].append(hurricanes[current_hurricane])
  return by_year


# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organize_by_year(hurricanes)
print("--------------")
print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas
def count_by_location(hurricanes):
  location_count = {}
  for record in hurricanes:
    for locations in hurricanes[record]["Areas Affected"]:
      if locations not in location_count:
        location_count[locations] = 1
      else:
        location_count[locations] +=1
  return location_count


# create dictionary of areas to store the number of hurricanes involved in
print("--------------")
by_location = count_by_location(hurricanes)
print(by_location)

# 5 
# Calculating Maximum Hurricane Count
def max_hurricanes(by_location):
  max_area = []
  max_area_count = 0
  for location in by_location:
    if by_location[location] > max_area_count:
      max_area = location
      max_area_count = by_location[location]
  return max_area, max_area_count


# find most frequently affected area and the number of hurricanes involved in
print("--------------")
print(max_hurricanes(by_location))

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  deadliest_hurricane = []
  deaths_hurricane = 0
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] > deaths_hurricane:
      deaths_hurricane = hurricanes[hurricane]["Deaths"]
      deadliest_hurricane = hurricanes[hurricane]["Name"]
  return deadliest_hurricane, deaths_hurricane




# find highest mortality hurricane and the number of deaths
print("--------------")
print(deadliest_hurricane(hurricanes))

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_hurricanes(hurricanes):
  mortality_dict = {0:[], 1:[] , 2:[] , 3:[] , 4:[], 5:[] }
  for record in hurricanes:
    if hurricanes[record]["Deaths"] == mortality_scale[0]:
      mortality_dict[0].append(hurricanes[record])
    elif hurricanes[record]["Deaths"] <  mortality_scale[1]:
      mortality_dict[1].append(hurricanes[record])
    elif hurricanes[record]["Deaths"] < mortality_scale[2]:
      mortality_dict[2].append(hurricanes[record])
    elif hurricanes[record]["Deaths"] < mortality_scale[3]:
      mortality_dict[3].append(hurricanes[record])
    elif hurricanes[record]["Deaths"] < mortality_scale[4]:
      mortality_dict[4].append(hurricanes[record])
    else:
      mortality_dict[5].append(hurricanes[record])
  return mortality_dict
# categorize hurricanes in new dictionary with mortality severity as key
print("--------------")
print(mortality_hurricanes(hurricanes)[5])

# 8 Calculating Hurricane Maximum Damage
def most_damage(hurricanes):
  damage_hurricane = []
  damage_amount = 0
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Damage"] == "Damages not recorded":
      continue
    if hurricanes[hurricane]["Damage"] > damage_amount:
      damage_amount = hurricanes[hurricane]["Damage"]
      damage_hurricane = hurricanes[hurricane]["Name"]
  return damage_hurricane, damage_amount

# find highest damage inducing hurricane and its total cost
print("--------------")
print(most_damage(hurricanes))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
def damage_rating(hurricanes):
  damage_dict = {"Damages not recorded": [], 0:[], 1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Damage"] == "Damages not recorded":
      damage_dict["Damages not recorded"].append(hurricanes[hurricane])
    elif hurricanes[hurricane]["Damage"] == damage_scale[0]:
      damage_dict[0].append(hurricanes[hurricane])
    elif hurricanes[hurricane]["Damage"] < damage_scale[1]:
      damage_dict[1].append(hurricanes[hurricane])
    elif hurricanes[hurricane]["Damage"] < damage_scale[2]:
      damage_dict[2].append(hurricanes[hurricane])
    elif hurricanes[hurricane]["Damage"] < damage_scale[3]:
      damage_dict[3].append(hurricanes[hurricane])
    elif hurricanes[hurricane]["Damage"] < damage_scale[4]:
      damage_dict[4].append(hurricanes[hurricane])
    else:
      damage_dict[5].append(hurricanes[hurricane])
  return damage_dict

# categorize hurricanes in new dictionary with damage severity as key
print("--------------")
print(damage_rating(hurricanes)[5])

