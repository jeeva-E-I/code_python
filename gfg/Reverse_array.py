# Reversing an array

arr = [1,2,0,4,3,0,5,0]
left = 0
right = len(arr) - 1
while left < right:
    arr[left] , arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)