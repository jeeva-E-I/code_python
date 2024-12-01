"""Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. 
    Find numbers a and b."""
def missing(arr):
    count_dict = {}
    result = 0
    for i in arr:
        if i in count_dict:
            count_dict[i] +=1
        else:
            count_dict[i] = 1
    arr = set(arr)
    positive =1
    for i in arr:
        if positive in arr:
            positive +=1
        if count_dict[i] > 1:
            result = i
    return [result,positive]

        
arr = [1, 2, 3, 4]
print(missing(arr))