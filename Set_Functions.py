#Example of built in functions of Set function

cars1 ={"bmw","suzuki","tata","audi"}
cars2 = cars1.copy()
#difference add
cars1.add("porsche") 
print(cars1)

#difference update
cars1.difference_update(cars2)
print(cars1)

#discard function
cars2.discard("suzuki")
print(cars2) 
cars1.add("bmw")

#intersection
print(cars1.intersection(cars2)) 
all_cars ={"bmw","suzuki","tata","audi","porsche","nissan"}

#issubset function
print(all_cars.issubset(cars2)) 
print(cars2.issubset(all_cars))

#pop function
all_cars.pop() 
print(all_cars)

#symmetric difference function
print(all_cars.symmetric_difference(cars1)) 

print(cars1.union(cars2)) #union function
