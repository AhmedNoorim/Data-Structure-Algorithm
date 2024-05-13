from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.__insert_recursive(self.root, value)

    # binary search insertion logic (type 1)
    def __insert_recursive(self, current_node: TreeNode, value):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = TreeNode(value)
            else:
                self.__insert_recursive(current_node.left, value)

        if value > current_node.value:
            if current_node.right == None:
                current_node.right = TreeNode(value)
            else:
                self.__insert_recursive(current_node.right, value)

    # binary search insertion logic (type 2)
    def __insert_recursive_1(self, current_node: TreeNode, value):
        if current_node == None:
            return TreeNode(value)

        if value < current_node.value:
            current_node.left = self.__insert_recursive_1(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__insert_recursive_1(current_node.right, value)

        return current_node

    def preorder_traversal(self):
        self.__preorder(self.root)
        print()

    def __preorder(self, current_node: TreeNode):

        if current_node != None:
            print(current_node.value, end=" ")
            self.__preorder(current_node.left)
            self.__inorder(current_node.right)

    def inorder_traversal(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, current_node: TreeNode):
        if current_node != None:
            self.__inorder(current_node.left)
            print(current_node.value, end=" ")
            self.__inorder(current_node.right)

    def postorder_traversal(self):
        self.__postorder(self.root)
        print()

    def __postorder(self, current_node: TreeNode):
        if current_node != None:
            self.__postorder(current_node.left)
            self.__postorder(current_node.right)
            print(current_node.value, end=" ")

    def search(self, value):
        return self.__search(self.root, value)

    def __search(self, node: TreeNode, value):
        if node == None:
            return "Does not Exist"

        if node.value == value:
            return "Value Exists"

        if value < node.value:
            return self.__search(node.left, value)
        if value > node.value:
            return self.__search(node.right, value)

    def delete(self, value):
        self.__delete(self.root, value)

    def __delete(self, current_node: TreeNode, value):
        if current_node == None:
            return current_node

        if value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete(current_node.right, value)

        if current_node.value == value:
            # for nodes with single child
            if current_node.left == None and current_node.right != None:
                return current_node.right
            elif current_node.left != None and current_node.right == None:
                return current_node.left

            # for nodes with no child
            if current_node.left == None and current_node.right == None:
                return None

            # for nodes with both child
            if current_node.left != None and current_node.right != None:
                lowest_right_value = self.__min_value(current_node)
                current_node.right = self.__delete(
                    current_node.right, lowest_right_value
                )
                current_node.value = lowest_right_value

        return current_node

    def __min_value(self, node: TreeNode):
        min_value = node.value
        while node.left != None:
            min_value = node.left.value
            node = node.left
            return min_value

    def BFS(self):
        if self.root == None:
            return "Empty Tree"

        current_node = self.root
        Q = deque()
        Q.append(current_node)

        while Q:
            current_node = Q.popleft()
            print(current_node.value, end=" ")
            if current_node.left:
                Q.append(current_node.left)
            if current_node.right:
                Q.append(current_node.right)


myTree = BinaryTree()
myTree.insert(5)
myTree.insert(3)
myTree.insert(7)
myTree.insert(2)
myTree.insert(4)
myTree.insert(6)
myTree.insert(8)

# duplicate insert
myTree.insert(4)


print("Preorder Traversal:", end=" ")
myTree.preorder_traversal()
print("Inorder Traversal:", end=" ")
myTree.inorder_traversal()
print("Postorder Traversal:", end=" ")
myTree.postorder_traversal()

print("Search 7: ", myTree.search(7))

myTree.delete(4)

print("Preorder Traversal:", end=" ")
myTree.preorder_traversal()
print("Inorder Traversal:", end=" ")
myTree.inorder_traversal()
print("Postorder Traversal:", end=" ")
myTree.postorder_traversal()


print("BFS: ", end=" ")
myTree.BFS()
