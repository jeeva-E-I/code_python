#Map function 
l1 = [1,2,3,4,5,6]
l2 = map(lambda x: x*2,l1)
print(list(l2))

#Filter function
def condition(x):
    if x<=3:
        return True
    else:
        return False

results = filter(condition,l1)
print(list(results))