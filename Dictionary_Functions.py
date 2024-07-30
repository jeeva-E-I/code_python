#DICTIONARY FUNCTIONS
import ast
dic1 ={
    "Name": 'james',
    "City": 'bangaluru',
    "age": 21,
    "Cars": ['audi','BMW','Tesla','ferrai']
    
}
city=('vellore','chennai','salem','trichy','madurai','thirupathur')
print(dic1)
print(dic1["age"])  #to print selected values using key 
print(dic1.get("City")) #To print the particular value in a dictionary using get method and key value
print(dic1.keys()) # To get key values in the dict
print(dic1.values()) # To get the values in the dict
print(dic1.items()) # To get the key value pair in the dict by creating a tupule

#conversion of string into a dict

str = "{'player_name': 'dhoni','Runs':5965,'Matches':376}"
d1 = ast.literal_eval(str)   # we need to import the ast package to convert a str into dict
print(d1)

dict ={"name":"jeeva","age":20}
dict2 = dict.copy() #Copy function
print(dict2)

pin =(66)
dict3 =dict.fromkeys(city,pin) #fromkeys function
print(dict3)

print(dict.get("age")) #get method

print(dict.items()) #Items function

dict3.pop("thirupathur")
print(dict3) #pop function

dict2.popitem()
print(dict2) #popitem function

dict3.setdefault("ooty",66) #Set default
print(dict3)

dict2.update({"college":"Amcet"}) #update function
print(dict2)

#Nested dictionary example

book= {1:{"name":"python","isbn":2712,"department":"cse"},
       2:{"name":"DBMS","isbn":4120,"department":"Cse"},
       3:{"name":"Embedded system","isbn":7120,"department":"ECE"}}
print(book[1])
print(book[2])
print(book[3]['isbn'])

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]
print(travel_log[0]["cities_visited"])
