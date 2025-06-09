class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def _init_(self):
        self.head = None

    # 1. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
            return
        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    # 2. Insert at beginning
    def insert_at_beginning(self, data):
        self.insert_at_end(data)
        self.head = self.head.prev

    # 3. Remove by value
    def remove_by_value(self, value):
        if not self.head:
            print("The list is empty.")
            return
        curr = self.head
        found = False
        while True:
            if curr.data == value:
                found = True
                break
            curr = curr.next
            if curr == self.head:
                break
        if not found:
            print(f"Value {value} not found in the list.")
            return
        if curr.next == curr:  # only one node
            self.head = None
            return
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        if curr == self.head:
            self.head = curr.next

    # 4. Display forward
    def show_list_forward(self):
        if not self.head:
            print("The list is empty.")
            return
        result = []
        curr = self.head
        while True:
            result.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(result))

    # 5. Display backward
    def show_list_backward(self):
        if not self.head:
            print("The list is empty.")
            return
        result = []
        curr = self.head.prev
        while True:
            result.append(str(curr.data))
            curr = curr.prev
            if curr.next == self.head.prev:
                break
        print(" <- ".join(result))

# Example usage
if _name_ == "_main_":
    cdll = CircularDoublyLinkedList()
    cdll.insert_at_end(10)
    cdll.insert_at_beginning(5)
    cdll.insert_at_end(15)
    cdll.show_list_forward()     
    cdll.show_list_backward()   
    cdll.remove_by_value(10)
    cdll.show_list_forward()     
    cdll.remove_by_value(99)     
    cdll.remove_by_value(5)
    cdll.remove_by_value(15)
    cdll.show_list_forward()