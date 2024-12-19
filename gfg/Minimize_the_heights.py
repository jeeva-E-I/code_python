k = 30
arr = [14, -92, -59, -41, -28, -89]
arr.sort()
new_min = arr[0] + k
new_max = arr[1] - k
new_list = [new_min,new_max]
for i in range(1,len(arr)-1):
    if arr[i] + k < new_min:
        new_list.append(arr[i] + k)
    elif arr[i] - k > new_max:
        new_list.append(arr[i] - k)
    else:
        new_list.append(arr[i] + k)
new_list.sort()
print(new_list)
out_diff = max(new_list) - min(new_list)
print(out_diff)




