import ctypes


class Stack:
    def __init__(self) -> None:
        self.top = None

        self.size = 1
        self.filled = 0

        self.stack = self.__make_array(self.size)

    def __make_array(self, capacity):
        # creates a C type array(static & referential) with size capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.filled

    def __resize_array(self, newSize):
        newArray = self.__make_array(newSize)

        for i in range(self.filled):
            newArray[i] = self.stack[i]

        self.stack = newArray

    def is_empty(self):
        return self.filled == 0

    def push(self, value):
        if self.size == self.filled:
            self.size += 4
            self.__resize_array(self.size)

        self.top = value
        self.stack[self.filled] = self.top
        self.filled += 1

    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            value = self.top

            self.filled -= 1
            if self.is_empty():
                self.top = None
            else:
                self.top = self.stack[self.filled - 1]

            return value

    def peek(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return self.top

    def traverse(self):
        for i in range(self.filled - 1, -1, -1):
            print(self.stack[i])


myStack = Stack()

print(myStack.is_empty())

myStack.push("1st entry")
myStack.push("2nd entry")
myStack.push("3rd entry")
myStack.push("4th entry")

print(myStack.is_empty())

myStack.traverse()

print("Peek:", myStack.peek())

print("Pop1:", myStack.pop())
print("Pop2:", myStack.pop())
print("Pop3:", myStack.pop())
print("Pop4:", myStack.pop())
print("Pop5:", myStack.pop())
