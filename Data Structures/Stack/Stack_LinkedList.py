class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.nodeCount = 0

    def is_empty(self):
        return self.top == None

    def push(self, value):
        newTop = Node(value)
        newTop.next = self.top
        self.top = newTop
        self.nodeCount += 1

    def pop(self):
        if self.is_empty():
            return "Empty Stack"

        value = self.top.value
        self.top = self.top.next
        self.nodeCount -= 1
        return value

    def peek(self):
        if self.is_empty():
            return "Empty Stack"

        return self.top.value

    def traverse(self):
        currentNode = self.top

        while currentNode != None:
            print(currentNode.value)
            currentNode = currentNode.next

    def __len__(self):
        return self.nodeCount


myStack = Stack()

print(myStack.is_empty())

myStack.push("Hello")
myStack.push(2024)
myStack.push("World")
myStack.push(13.13)
myStack.push("Bye")

print(myStack.is_empty())

myStack.traverse()

print(myStack.pop())

print(myStack.peek())
print(len(myStack))
