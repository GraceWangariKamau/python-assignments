class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

node1 = LinkedListNode("5")
node2 = LinkedListNode("6")
node3 = LinkedListNode("7")
node4 = LinkedListNode("8")
node5 = LinkedListNode("9")
node6 = LinkedListNode("10") 
node7 = LinkedListNode("11")
node8 = LinkedListNode("12")
node9 = LinkedListNode("13")
node10 = LinkedListNode("14")       

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8
node8.nextNode = node9
node9.nextNode = node10

currentNode = node1 
while True:
    print(currentNode.value, ">>>", end=" ")

    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode
