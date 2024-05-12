class Dictionary:

    def __init__(self, size) -> None:
        self.size = size

        # declaring fixed size array like C
        self.keys = [None] * self.size
        self.data = [None] * self.size

    def __hash_function(self, key):
        # hash() -> generates hash value for immutable type data
        return abs(hash(key)) % self.size

    def __rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.__hash_function(key)

        if self.keys[hash_value] == None:
            self.keys[hash_value] = key
            self.data[hash_value] = value

        else:
            # key already exists on the position
            if self.keys[hash_value] == key:
                self.data[hash_value] = value

            # some other key exists on the position
            else:
                new_hash_value = self.__rehash(hash_value)
                while (
                    self.keys[new_hash_value] != None
                    and self.keys[new_hash_value] != value
                ):
                    new_hash_value = self.__rehash(new_hash_value)

                if self.keys[new_hash_value] == None:
                    self.keys[new_hash_value] = key
                    self.data[new_hash_value] = value

                if self.keys[new_hash_value] == key:
                    self.data[new_hash_value] = value

    def get(self, key):
        start_index = self.__hash_function(key)
        current_index = start_index

        while self.keys[current_index] != None:
            if self.keys[current_index] == key:
                return self.data[current_index]

            current_index = self.__rehash(current_index)

            if current_index == start_index:
                return "Not Found -> returned to first index"

        return "Not Found -> stopped at None"

    def remove(self, key):
        start_index = self.__hash_function(key)
        current_index = start_index

        while self.keys[current_index] != None:
            if self.keys[current_index] == key:
                self.keys[current_index] = None
                self.data[current_index] = None
                return "Remove Successful"

            current_index = self.__rehash(current_index)

            if current_index == start_index:
                return "Not Found"

        return "Not Found"

    # using {dictionary_name[key] = value} to set value
    def __setitem__(self, key, value):
        self.put(key, value)

    # using {dictionary_name[key]} to get value
    def __getitem__(self, key):
        return self.get(key)

    def __str__(self):
        result = ""
        for i in range(len(self.keys)):
            if self.keys[i] != None:
                result = result + str(self.keys[i]) + " : " + str(self.data[i]) + ", "

        return "[" + result[:-2] + "]"


myDictionary = Dictionary(4)

myDictionary.put("Python", 13)
print(myDictionary)

myDictionary["Java"] = 7
print(myDictionary)

myDictionary["Python"] = 100
myDictionary["C"] = 75
# myDictionary["C++"] = 63

print(myDictionary)

print(1)
print("Value:", myDictionary["Py"])

print(2)
print(myDictionary)

print(3)
print(myDictionary.remove("Java"))
print(myDictionary)
