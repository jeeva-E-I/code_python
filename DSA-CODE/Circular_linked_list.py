#CIRCULAR LINKED LIST
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self,data): # Insertion at the end
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head and current:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def prepand (self,data): # Insertion at the beginning
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current and current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insertion(self,data,position): # Inseration at the position
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            count = 0
            if position == 0:
                    self.prepand(data)
                    return
            while count < position-1 and current.next != self.head:
                count +=1
                current = current.next
            if count == position-1:
                new_node.next = current.next
                current.next = new_node
            else:
                print("Position out of range")    
                
    def delete_first_node(self):
        if not self.head:
            return
        else:
            current = self.head
            while current and current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
    def delete_last(self):
        if not self.head:
            return
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head
    def delete_data(self,data):
        if not self.head:
            return
        if self.head.data == data:
            self.delete_first_node()
            return
        prev = None
        current = self.head
        while current.next != self.head:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        if current.next == data:
            self.delete_last()
            return
            

    def display(self):
        current = self.head
        while True:
            print(current.data,end="-->")
            current = current.next
            if current == self.head:
                break
        print(None)
    

    

if __name__ == "__main__":
    Linked_list = Linkedlist()
    Linked_list.append(0)
    Linked_list.append(1)
    Linked_list.append(2)
    Linked_list.display()
    Linked_list.insertion(3,3)
    Linked_list.display()
    Linked_list.delete_first_node()
    Linked_list.delete_last()
    Linked_list.display()