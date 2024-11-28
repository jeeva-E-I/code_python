def missing(arr):
        result = 0
        arr.sort()
        new_set = set(arr)
        positive = 1
        while positive in new_set:
            if arr.count(positive) >1:
                result = arr[positive]
            positive +=1
        return [result,positive]
        
arr = [7, 2, 3, 4, 5, 6, 6]
print(missing(arr))