import ctypes


class myList:

    def __init__(self):
        self.size = 1
        self.filled = 0

        # create a C type array with size
        self.array = self._make_array(self.size)

    def _make_array(self, capacity):
        # creates a C type array(static & referential) with size capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.filled

    def __str__(self):
        result = ""
        for i in range(self.filled):
            result += str(self.array[i]) + ", "

        return "[" + result[:-2] + "]"

    def __getitem__(self, index):
        if 0 <= index < self.filled:
            return self.array[index]
        else:
            return "IndexError: Index out of range"

    def _resize(self, newSize):
        newArray = self._make_array(newSize)
        self.size = newSize

        # copy content from array to newArray
        for i in range(self.filled):
            newArray[i] = self.array[i]

        self.array = newArray

    def __delitem__(self, index):
        if 0 <= index < self.filled:
            for i in range(index, self.filled - 1):
                self.array[i] = self.array[i + 1]

            self.filled -= 1

        else:
            return "IndexError: Index out of range"

    def append(self, item):
        if self.filled == self.size:
            self._resize(self.size * 2)

        self.array[self.filled] = item
        self.filled += 1

    def insert(self, value, index):
        if self.filled == self.size:
            self._resize(self.size * 2)

        for i in range(self.filled, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.filled += 1

    def remove(self, value):
        index = self.find(value)
        if type(index) == int:
            self.__delitem__(index)
        else:
            print("ValueError - Not in List")

    def pop(self):
        if self.filled == 0:
            return "Empty List"

        print(self.array[self.filled - 1])
        self.filled -= 1

    def clear(self):
        self.filled = 0
        self.size = 1

    def find(self, item):
        for i in range(self.filled):
            if self.array[i] == item:
                return i

        return "ValueError - Not in List"


Li = myList()

Li.append("Noorim")
Li.append(13)
Li.append(True)
Li.append(7.5)
Li.append("Smile")
Li.append(777)

print(Li[1])
print(Li)
print("Size:", len(Li))

Li.pop()
# Li.clear()
print(Li)

print(Li.find(7.5))
print(Li.find("No"))

Li.insert("Love", 2)
print(Li)

del Li[3]
print(Li)

Li.remove(13)
print(Li)
