#SINNGLY LINKED LIST
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #Keep track for next value

class Linkedlist:
    def __init__(self):
        self.head = None

    # add node to the end of the linked list
    def append(self,data):
        new_node = Node(data)
        if not self.head: # checks whether the head node is none or not. if none means condition true
            self.head = new_node # assigning the new_node has head node
        else:
            current = self.head
            while current.next: # it checks the next element has value or not.
                current = current.next # the value of nxt node is assigned to current node to find the null
            current.next = new_node

    # Prepand a new node to the beginning of the Linked list
    def prepand(self,data):
        new_node = Node(data)
        new_node.next = self.head # Adding the head value to the next of new node
        self.head = new_node # Assigning new node as head node

    # Delete a node with a specific value form the linked list
    def delete(self,data):
        if not self.head:
            return
        if self.head.data == data: # deleting a node at beginning
            self.head = self.head.next
            return
        
        current = self.head
        while current.next: #deletinng a node at the specified element
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    # Print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end ="--> ")
            current = current.next
        print(None)

#Example

if __name__ == "__main__":
    linked_list = Linkedlist()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    linked_list.display()

    linked_list.prepand(0)
    linked_list.display()

    linked_list.delete(2)
    linked_list.display()

    linked_list.prepand(1.5)
    