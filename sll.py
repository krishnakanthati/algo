# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty!")
            return

        currentNode = self.head
        while True:
            if currentNode is None:
                print(None)
                break
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next



firstNode = Node("John")
secondNode = Node("Ben")
thirdNode = Node("Kris")

linkedList = LinkedList()

linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)

linkedList.printList() # John -> Ben -> Kris -> None