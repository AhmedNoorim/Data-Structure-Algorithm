class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:

    # constructor
    def __init__(self):
        self.head = None

    def add(self, key, value):
        newNode = Node(key, value)

        if self.head == None:
            self.head = newNode

        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = newNode

    def remove(self, key):
        if self.head == None:
            return "Empty"
        else:
            if self.head.key == key:
                self.head = self.head.next
            else:
                currentNode = self.head
                while currentNode.next != None:
                    if currentNode.next.key == key:
                        break
                    currentNode = currentNode.next

                if currentNode.next == None:
                    return "Not Found"
                else:
                    currentNode.next = currentNode.next.next

    def search(self, key):
        currentNode = self.head
        n = 0
        while currentNode != None:
            if currentNode.key == key:
                return n
            currentNode = currentNode.next
            n += 1

        return -1

    def traverse(self):
        currentNode = self.head
        result = ""
        while currentNode != None:
            result += str(currentNode.key) + ":" + str(currentNode.value) + ", "
            currentNode = currentNode.next
        print("[", result[:-2], "]")

    def get_node_at_index(self, index):
        if self.head == None:
            return None

        temp_node = self.head
        while index:
            temp_node = temp_node.next
            index -= 1
        return temp_node


class Dictionary:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # creating array of linked list
        self.buckets = self.__make_array(self.capacity)

    def __make_array(self, capacity):
        L = []
        for i in range(capacity):
            L.append(LinkedList())
        return L

    def __hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def __get_node_index(self, bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index

    def __put(self, key, value):
        bucket_index = self.__hash_function(key)

        node_index = self.__get_node_index(bucket_index, key)
        if node_index == -1:
            # insert
            self.buckets[bucket_index].add(key, value)
            self.size += 1

            # load factor -- causes rehashing
            load_factor = self.size / self.capacity

            #! check - start
            # # for checking
            # print("LoadFactor for capacity {}:".format(self.capacity), load_factor)
            #! check - end

            if load_factor >= 2:
                self.__rehash()

        else:
            # update
            temp_node = self.buckets[bucket_index].get_node_at_index(node_index)
            temp_node.value = value

    def __get(self, key):
        bucket_index = self.__hash_function(key)

        item_index = self.buckets[bucket_index].search(key)
        if item_index == -1:
            return "Item Does Not Exist"
        else:
            temp_node = self.buckets[bucket_index].head
            while item_index:
                temp_node = temp_node.next
                item_index -= 1
            return temp_node.value

    def __delete(self, key):
        bucket_index = self.__hash_function(key)
        item_in_list = self.buckets[bucket_index]
        item_in_list.remove(key)
        self.size -= 1

    def __traverse(self):
        result = ""
        for i in self.buckets:
            temp_node = i.head
            while temp_node != None:
                result += str(temp_node.key) + ":" + str(temp_node.value) + ", "
                temp_node = temp_node.next

        return "[" + result[:-2] + "]"

    #! important
    def __rehash(self):
        # double the capacity
        self.capacity *= 2
        # storing buckets in old_buckets
        old_buckets = self.buckets
        # overwriting buckets with a new empty array(new capacity)
        self.size = 0
        self.buckets = self.__make_array(self.capacity)

        # getting LinkedList for each index of old_buckets
        for i in old_buckets:
            # getting the 1st item of LinkedList i
            temp = i.head
            while temp != None:
                # putting key and value to "buckets"
                self.__put(temp.key, temp.value)
                temp = temp.next

    # taking input
    def __setitem__(self, key, value):
        self.__put(key, value)

    # getting output - value
    def __getitem__(self, key):
        return self.__get(key)

    # deleting a value by key
    def __delitem__(self, key):
        return self.__delete(key)

    # printing dictionary
    def __str__(self):
        return self.__traverse()

    # getting size of dictionary
    def __len__(self):
        return self.size


myDictionary = Dictionary(3)

myDictionary["Python"] = 90
myDictionary["Java"] = 70
myDictionary["C"] = 60
myDictionary["C++"] = 80
myDictionary["C#"] = 65
myDictionary["Kotlin"] = 50
myDictionary["React"] = 70
myDictionary["Python"] = 100  # update
myDictionary["Ruby"] = 40


#! check - start
# # check each LinkedList for index of dictionary array
# def check(dictionary: Dictionary):
#     for i in range(dictionary.capacity):
#         print("{}:".format(i), end="")
#         myDictionary.buckets[i].traverse()


# check(myDictionary)
#! check - end

del myDictionary["Java"]
print(myDictionary["Java"])

print("My Dictionary:", myDictionary)
print("Size:", len(myDictionary))
