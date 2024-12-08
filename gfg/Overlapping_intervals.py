#Overlapping intervals
"""Given an array of Intervals arr[][], where arr[i] = [starti, endi]. 
    The task is to merge all of the overlapping Intervals."""

""" 1. sort the given arr[][] and initialize index = 0
    2. traverse from to 1 to end of the array. Two intervals arr[index][start1,end1] and arr[i][start2,end2]

    3. check overlap condition { start2 <= end1 } means update arr[index][1] = max(arr[index][1],arr[i][1])
    4. else increment index and copy current interval arr[i] to arr[index]
    5. return arr[:index+1]
"""

def overlapping(): #Space complexity O(1)
    arr =  [[1,3],[2,6],[8,10],[15,18]]
    arr.sort()
    index = 0
    for i in range(1,len(arr)):
        if arr[i][0] <= arr[index][1]:
            arr[index][1] = max(arr[index][1],arr[i][1])
        else:
            index += 1
            arr[index] = arr[i]
    print(arr[:index+1])
    # print(arr)


# overlapping()

def Overlapping(): #Space complexity is O(n)
    arr = [[1,3],[2,6],[8,10],[15,18]]
    arr.sort()
    merged = [arr[0]]
    index = 0
    for i in arr:
        if i[0] <= merged[0][1]:
            merged[index] = [merged[index][0],max(i[1],merged[index][1])]
        else:
            merged.append(i)
            index += 1

    print(merged)

Overlapping()

# Time complexity = O(nlogn)