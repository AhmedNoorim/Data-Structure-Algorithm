class CircularNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    # constructor
    def __init__(self):
        self.head = None
        self.nodeCount = 0

    #! let use len()
    def __len__(self):
        return self.nodeCount

    #! return a string for print()
    def __str__(self):
        result = "LinkedList: "
        currentNode = self.head

        while self.head != None:
            result = result + str(currentNode.value) + " -> "
            currentNode = currentNode.next

            if currentNode == self.head:
                break

        return result[:-4] if self.head != None else "Empty LinkedList"

    def appendValue(self, value):
        newNode = CircularNode(value)

        if self.nodeCount == 0:
            self.head = newNode
            self.head.next = self.head

        else:

            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next

            newNode.next = self.head
            currentNode.next = newNode

        self.nodeCount += 1

    def insertBeginning(self, value):
        newNode = CircularNode(value)

        if self.nodeCount == 0:
            print("Append the 1st item")
            return "Append the 1st item"

        currentNode = self.head.next
        while currentNode.next != self.head:
            currentNode = currentNode.next

        newNode.next = self.head
        self.head = newNode
        currentNode.next = self.head

        self.nodeCount += 1

    def insertAfter(self, value, prevIndex):
        newNode = CircularNode(value)
        currentNode = self.head

        if prevIndex >= self.nodeCount:
            print("Index Limit Exceeded")
            return "Index Limit Exceeded"

        n = 0
        while n != prevIndex:
            currentNode = currentNode.next
            n += 1

        newNode.next = currentNode.next
        currentNode.next = newNode
        self.nodeCount += 1

    def clearLinkedList(self):
        self.head = None
        self.nodeCount = 0

    def deleteHead(self):
        if self.head == None:
            print("It is an empty LinkedList")
            return "It is an empty LinkedList"

        currentNode = self.head.next
        while currentNode.next != self.head:
            currentNode = currentNode.next

        self.head = self.head.next
        currentNode.next = self.head

        self.nodeCount -= 1

    def pop(self):
        if self.head == None:
            print("It is an empty LinkedList")
            return "It is an empty LinkedList"

        currentNode = self.head
        while currentNode.next.next != self.head:
            currentNode = currentNode.next

        currentNode.next = self.head
        self.nodeCount -= 1

    def removeIndex(self, index):
        if self.head == None:
            print("It is an empty LinkedList")
            return "It is an empty LinkedList"

        if index >= self.nodeCount:
            print("Index Limit Exceeded")
            return "Index Limit Exceeded"

        if index == 0:
            return self.deleteHead()

        currentNode = self.head

        n = 0
        while n != index - 1:
            currentNode = currentNode.next
            n += 1

        currentNode.next = currentNode.next.next
        self.nodeCount -= 1

    def search(self, value):
        currentNode = self.head
        n = 0
        while True:
            if currentNode.value == value:
                print("Item found at index", n)
                return n
            currentNode = currentNode.next
            n += 1
            if currentNode == self.head:
                break

        print("Item not found")
        return -1

    #! return item like LL[index]
    def __getitem__(self, index):
        currentNode = self.head
        n = 0
        while True:
            if n == index:
                return currentNode.value
            currentNode = currentNode.next
            n += 1
            if currentNode == self.head:
                break

        print("Index Limit Exceeded")
        return "Index Limit Exceeded"


myLinkList = LinkedList()

myLinkList.appendValue(13)
print(myLinkList)
print(len(myLinkList))

myLinkList.insertBeginning(133)
print(myLinkList)
print(len(myLinkList))

myLinkList.appendValue(70)
myLinkList.appendValue(95)
myLinkList.appendValue(65)
# myLinkList.appendValue(35)
# myLinkList.appendValue(15)
print(myLinkList)
print(len(myLinkList))

myLinkList.insertAfter(27, 1)
print(myLinkList)
print(len(myLinkList))

# # myLinkList.clearLinkedList()
myLinkList.deleteHead()
print(myLinkList)
print(len(myLinkList))

myLinkList.pop()
print(myLinkList)
print(len(myLinkList))

myLinkList.removeIndex(1)
print(myLinkList)
print(len(myLinkList))

myLinkList.search(95)

print(myLinkList[1])
