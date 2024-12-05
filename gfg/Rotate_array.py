# Rotating array for d times

""" We will use reversal algorithm to rotate an array
    1. Reverse the first 'd' elements
    2. Reverse the last elements from d to end of the array
    3. Reverse the whole array
"""

def reversal(arr,start,stop):
    while start < stop:
        arr[start] , arr[stop] = arr[stop] , arr[start]
        start += 1
        stop -= 1
        return arr

arr = [7,3,9,1]
d = 9

length = len(arr)
d %= length # if  the size of the array is less than the value of d means it should minimise it

reversal(arr,0,d-1)
reversal(arr,d,length-1)
reversal(arr,0,length-1)

print(arr)