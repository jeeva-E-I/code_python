#KADANE'S ALGORITHM
""" Kadane's Algorithm is a popular and efficient algorithm to find the maximum sum of a 
    contiguous subarray within a one-dimensional array of numbers"""

# STEP 1 : Initialise variable max_arr and current_arr
# STEP 2 : Transverse the array
# STEP 3 : update current sum by deciding whether to 
#         (i)  Add the current element to current_sum (extending the current subarray), or
#         (ii) Start a new subarray with just the current element.
# STEP 4 : update the max-sum
# STEP 5 : End of iteration. return the maximum sum

arr = [2, 3, -8, 7, -1, 2, 3]
current_sum = arr[0]
max_sum = arr[0]
for i in range(1,len(arr)):
    current_sum = max(current_sum + arr[i],arr[i])        
    max_sum = max(current_sum,max_sum)
print(max_sum)