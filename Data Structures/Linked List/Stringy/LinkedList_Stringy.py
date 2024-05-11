class StringyNode:
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

        while currentNode != None:
            result = result + str(currentNode.value) + " -> "
            currentNode = currentNode.next

        return result[:-4] if self.head != None else "Empty LinkedList"

    def insertHead(self, value):
        newNode = StringyNode(value)
        newNode.next = self.head
        self.head = newNode
        self.nodeCount += 1

    def appendValue(self, value):
        newNode = StringyNode(value)
        currentNode = self.head

        while currentNode.next != None:
            currentNode = currentNode.next

        currentNode.next = newNode

        self.nodeCount += 1

    def insertAfter(self, value, prevIndex):
        newNode = StringyNode(value)
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

        self.head = self.head.next
        self.nodeCount -= 1

    def pop(self):
        if self.head == None:
            print("It is an empty LinkedList")
            return "It is an empty LinkedList"

        if self.nodeCount == 1:
            return self.deleteHead()

        currentNode = self.head
        while currentNode.next.next != None:
            currentNode = currentNode.next

        currentNode.next = None
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
        while currentNode != None:
            if currentNode.value == value:
                print("Item found at index", n)
                return n
            currentNode = currentNode.next
            n += 1

        print("Item not found")
        return -1

    #! return item like LL[index]
    def __getitem__(self, index):
        currentNode = self.head
        n = 0
        while currentNode != None:
            if n == index:
                return currentNode.value
            currentNode = currentNode.next
            n += 1

        print("Index Limit Exceeded")
        return "Index Limit Exceeded"

    def reverseLinkedList(self):
        prevNode = None
        currentNode = self.head

        while currentNode != None:
            bufferNode = currentNode
            currentNode = currentNode.next

            bufferNode.next = prevNode
            prevNode = bufferNode

        self.head = prevNode


myLinkList = LinkedList()

myLinkList.insertHead(13)
print(myLinkList)
print(len(myLinkList))

myLinkList.insertHead(133)
print(myLinkList)
print(len(myLinkList))

myLinkList.appendValue(70)
myLinkList.appendValue(95)
myLinkList.appendValue(65)
myLinkList.appendValue(35)
myLinkList.appendValue(15)
print(myLinkList)
print(len(myLinkList))

myLinkList.insertAfter(27, 1)
print(myLinkList)
print(len(myLinkList))

# myLinkList.clearLinkedList()
myLinkList.deleteHead()
print(myLinkList)
print(len(myLinkList))

myLinkList.pop()
print(myLinkList)
print(len(myLinkList))

myLinkList.removeIndex(0)
print(myLinkList)
print(len(myLinkList))

myLinkList.search(65)

print(myLinkList[2])

myLinkList.reverseLinkedList()
print(myLinkList)
