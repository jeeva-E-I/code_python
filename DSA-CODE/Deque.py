#DOUBLE ENDED QUEUE
from collections import deque

queue = deque()

#Addition of elements in deque
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

front = queue[0]
rear = queue[-1]
print(queue)
print("Front: ", front)
print("Rear: ",rear)

#Deletion of elements in deque
element_1 = queue.popleft()
element_2 = queue.popleft()
element_3 = queue.popleft()

#To check queue is empty or not
def isempty():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue is not empty")
        
isempty()
print(queue)