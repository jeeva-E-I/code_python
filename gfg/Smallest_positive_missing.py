def smallest_missing(arr):

    arr.sort()
    if arr == []:
            print(1)
    for i in range(1,len(arr)+1):
        if i not in arr:
            print(i)
    # print(len(arr)+1)

arr = [1, 2, 2, 3, 4, 5]
smallest_missing(arr)