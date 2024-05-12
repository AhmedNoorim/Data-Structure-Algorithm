class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self):
        self.root = None
        self.__node_list = []

    def add(self, parent_value, value):
        if value in self.__node_list:
            return False

        new_node = TreeNode(value)

        if self.root == None:
            self.root = new_node
            self.__node_list.append(new_node.value)
            return True

        parent_node = self.__find_node(self.root, parent_value)
        if parent_node:
            parent_node.children.append(new_node)
            self.__node_list.append(new_node.value)
            return True
        return False

    def __find_node(self, current_node: TreeNode, value):
        if current_node.value == value:
            return current_node

        for child in current_node.children:
            found_node = self.__find_node(child, value)
            if found_node:
                return found_node
        return None

    def __print_tree(self, current_node: TreeNode, level):

        print("  " * level + str(current_node.value))
        for child in current_node.children:
            self.__print_tree(child, level + 1)

    def __str__(self):
        self.__print_tree(self.root, 0)
        return ""

    def print_children(self, node_value):
        node = self.__find_node(self.root, node_value)
        if node:
            print(node.value, end=" -> ")
            for i in node.children:
                print(i.value, end=" ")
        else:
            "Node does not exist"

    def find(self, value):
        return value in self.__node_list

    def traverseBFS(self, node=None):
        current_level = []

        if node == None:
            print(self.root.value, end=" ")
            current_level = self.root.children

        else:
            current_level = node.children

        for i in current_level:
            print(i.value, end=" ")

        for i in current_level:
            self.traverseBFS(i)


myTree = Tree()

myTree.add(None, 1)
myTree.add(1, 2)
myTree.add(1, 3)
myTree.add(1, 4)
myTree.add(2, 5)
myTree.add(2, 6)
myTree.add(3, 7)
myTree.add(4, 8)
myTree.add(4, 9)
myTree.add(4, 10)


print("Tree:")
print(myTree)

# for i in range(1, 11):
#     myTree.print_children(i)
#     print()

print(myTree.find(0))

print("BFS: ", end=" ")
myTree.traverseBFS()
