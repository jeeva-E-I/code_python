class CircularQueue:
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.queue = [0] * size
        self.size = size
    
    def enqueue(self,item):
        if self.front == -1: # checks whether the queue is empty or not
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size # if it is not empty queue means increment the rear value by 1 by (i+1)% size
            if self.rear == self.front: # after increments it checks whether the value is equal to front value that (4+1)%5 = 0 i.e front value
                self.rear = (self.rear-1 + self.size) % self.size # it reduces the value back to i from i+1
                return "Queue is full cannot do enqueue operation"
            else:
                self.queue[self.rear] = item
    
    def dequeue(self):
        value = -1
        if not self.front == -1: # empty queue
            value = self.queue[self.front] 
            if self.front == self.rear: # if it has only one element reset the queue
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size # increment the front value by 1
        else:   
            return "Queue is empty"
        return value
    
    def peek(self):
        if not self.front == -1:
            return self.queue[self.front]
        else:
            return "Queue is empty"
        
    def isEmpty(self):
        return self.front ==-1
    
    def display(self):
        for i in range(self.size-1,self.front-1,-1):
            print(self.queue[i], end=" ")
        print(end='\n')
        
        
circular_queue = CircularQueue(5)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)
circular_queue.display()
# print(circular_queue.rear)
# print(circular_queue.front)
print(circular_queue.dequeue())
peek_value = circular_queue.peek()
print(peek_value)
circular_queue.display()

        