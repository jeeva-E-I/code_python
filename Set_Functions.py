#Example of built in functions of Set function

cars1 ={"bmw","suzuki","tata","audi"}
cars2 = cars1.copy()
cars1.add("porsche") #difference add
print(cars1)
cars1.difference_update(cars2) #difference update
print(cars1)
cars2.discard("suzuki")
print(cars2) #discard function
cars1.add("bmw")
print(cars1.intersection(cars2)) #intersection
all_cars ={"bmw","suzuki","tata","audi","porsche","nissan"}
print(all_cars.issubset(cars2)) #issubset function
print(cars2.issubset(all_cars))
all_cars.pop() #pop function
print(all_cars)
print(all_cars.symmetric_difference(cars1)) #symmetric difference function
print(cars1.union(cars2)) #union functio
