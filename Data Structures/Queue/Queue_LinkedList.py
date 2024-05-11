class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.counter = 0

    def enqueue(self, value):
        newNode = Node(value)

        if self.rear == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        self.counter += 1

    def dequeue(self):
        if self.front == None:
            return "Empty Queue"
        else:
            value = self.front.value
            self.front = self.front.next
            self.counter -= 1
            return value

    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.value, end=", ")
            temp = temp.next

    def is_empty(self):
        return self.front == None

    def peekFront(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            return self.front.value

    def peekRear(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            return self.rear.value


Q = Queue()

Q.enqueue("1st entry")
Q.enqueue("2nd entry")
Q.enqueue("3rd entry")
Q.enqueue("4th entry")

Q.traverse()

Q.dequeue()
print()

Q.traverse()

print("\nFront: ", Q.peekFront())
print("Rear: ", Q.peekRear())
