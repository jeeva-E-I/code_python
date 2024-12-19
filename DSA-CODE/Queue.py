# QUEUE IMPLEMENTATION
from queue import Queue
que =  Queue(maxsize= 5) #Number of items allowed in the queue

#Enqueue method : put()

que.put(1)
que.put(2)
que.put(3)

que.put_nowait(4) # equivalent to put(item,block = True)
que.put(5)
# que.put(6)# If we add an element exceeding the limit of the queue the queue will be in blocked state
# que.put(6,block=False) """To avoid blocking state we use block to false which will immediately raises queue.full"""
# que.put(6,timeout= 5) """ If we use timeout it will hold for a seconds and raises queue.full {used in try and except}"""

print(que.qsize()) # return length of the queue

print(que.full()) # checks whether the queue is full  or not
print(que.empty()) # checks whether queue is empty


# # print values of the queue without deleting element
# temp = []
# print("Queue:",end=" ")
# while not que.empty():
#     value = que.get() #get method is used to pop the element
#     print(value, end=" ")
#     temp.append(value)
# #re add the values to queue
# for item in temp:
#     que.put(item)

#Print values of queue
print("Queue")
while not que.empty():
    value = que.get()
    print(value)
