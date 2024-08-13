# Built in functions of list

name1 = ["arun","akash","charran"]
name2 = ["akshaya","abinaya","banu","bhuva"]

#append function
name1.append("denver") 
print(name1)

# copy function
name3 = name2.copy()
print(name3)

# Count function
print(name1.count('charran')) 

#Extend function
name1.extend(name2) 
print(name1)

#index function
print(name1.index("akshaya")) 

#pop function
print(name1.pop(5)) 

# insert function
name1.insert(6, "chithra") 
print(name1)

#remove function
name2.remove("bhuva")
print(name2)

#Reverse function
name1.reverse() 
print(name1)

#Sort function
name1.sort() 
print(name1)