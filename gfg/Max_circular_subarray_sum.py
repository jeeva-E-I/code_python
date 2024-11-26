arr = [-7, 32, -11, 21, 18, 35, -26, -17, 35, -12, -38, -33, 32, 16, 44, 11, -40, -21, 2, 27, -35, 21, -37, -12, 1]
def max_circular_subarray_sum(arr):
    total_sum = sum(arr)
    current_sum = max_linear_sum = arr[0]

    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_linear_sum = max(max_linear_sum, current_sum)

    for i in range(len(arr)):arr[i] = arr[i] * -1 
    
    current_sum = max_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    max_sum = max_sum * -1
    max_circular_sum = total_sum - max_sum
    
    if max_circular_sum == 0:
        return max_linear_sum
    elif max_circular_sum < max_linear_sum:
        return max_linear_sum
    else:
        return max_circular_sum
print(max_circular_subarray_sum(arr))

