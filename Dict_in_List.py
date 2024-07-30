#Dictionary in list
def add_new_country(country_name,num_visits,cities_name):
  travel_log_dict ={
      "country": country_name,
      "visits": num_visits,
      "cities": cities_name
    }
  travel_log.append(travel_log_dict)

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string.... eval function converts the string expressions into particular python format

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")