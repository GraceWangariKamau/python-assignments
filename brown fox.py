class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def InsertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    llist = LinkedList()

    llist.InsertAtTheBeginning("Fox")
    llist.InsertAtTheBeginning("Brown")       
    llist.InsertAtTheBeginning("Quick")
    llist.InsertAtTheBeginning("The")

    llist.printLinkedList()

    llist.InsertAtTheEnd("Jumps")
    llist.InsertAtTheEnd("Over")
    llist.InsertAtTheEnd("Lazy")
    llist.InsertAtTheEnd("Dog")

    llist.printLinkedList()
