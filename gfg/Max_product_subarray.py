#MAXIMUM PRODUCT OF SUBARRAY

"""Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a subarray of arr."""

# STEP 1: Initialize Variables max_end,min_end,max_product as arr[0]
# STEP 2: Iterate through loops to identify the max_product
#           max_ending = max(arr[i], max_ending * arr[i])
#           min_ending = min(arr[i], min_ending* arr[i])
#           if arr[i] is negative swap max and min end 
# STEP 3: if arr[i] is zero reset min and max to zero and find sub array

arr = [-2, 6, -3, -10, 0, 2]
def max_product(arr): 
    max_ending= max_product = min_ending = arr[0]
    for i in range(1,len(arr)):
        if arr[i] == 0:
            max_ending = min_ending = 0
        if arr[i] < 1:
            temp = max_ending
            max_ending = min_ending
            min_ending = temp
        max_ending = max(arr[i], max_ending * arr[i])
        min_ending = min(arr[i], min_ending* arr[i])
        max_product = max(max_product , max_ending)
    return max_product
a = max_product(arr)
print(a)