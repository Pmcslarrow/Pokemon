#Paul McSlarrow Doubly Circular Linked List

class Node:
    def __init__(self, value):
        self.item = value
        self.next = None
        self.prev = None
        self.size = 0

    def get_item(self):
        return self.item

class DCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_current(self):
        return self.head

    def insert_item(self, new_item):
        if self.is_empty():
            self.head = Node(new_item)
            self.tail = self.head
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1

        elif self.size == 1:
            self.head.prev = Node(new_item)
            self.head.prev.next = self.head
            self.head.prev.prev = self.head
            self.head.next = self.head.prev
            self.tail = self.head.prev
            self.head = self.head
            self.size += 1

        else:
            previous = self.head.prev
            head = self.head
            new_node = Node(new_item)

            previous.next = new_node
            new_node.prev = previous

            new_node.next = head
            head.prev = new_node
            self.size += 1


    def remove_item_with_current(self, current):
        previous = current.prev
        infront = current.next

        previous.next = infront
        infront.prev = previous

        self.size -= 1

    def remove_item_with_index(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        
        previous = current.prev
        current = current
        infront = current.next

        previous.next = infront
        infront.prev = previous

        self.size -= 1


    #Friendly reminder that when searching for the item it counts from 0 first not 1...
    def index(self, item_to_search):
        current = self.head
        counter = 0
        while current.item != item_to_search:
            current = current.next
            counter += 1

        return counter

    def find_item_at_index(self, index):
        current = self.head
        if index == 0:
            return current.item
        else:
            for i in range(index):
                current = current.next
            return current.item

    def counter_index(self, counter):                #Everytime a user clicks, counter goes up. Now if we want the value stored at the spot, given the counter, I will use modulo to return the item
        return counter % self.size


    def __str__(self):
        if self.size == 1:
            print(self.head.item)
        else:
            counter = 0
            current = self.head
            while counter != self.size:
                print(current.item)
                current = current.next
                counter += 1

    def __getitem__(self, index):
        current = self.head
        if index == 0:
            return current.item
        else:
            for i in range(index):
                current = current.next
            return current.item


