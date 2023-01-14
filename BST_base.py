import random as rand

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # if node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def search(self, val):
        if self.data == val:
            return "Found"

        if val < self.data:
            if self.left: # check val in left subtree
                return self.left.search(val)
            else:
                return "Not Found"

        if val > self.data:
            if self.right: # check val in right subtree
                return self.right.search(val)
            else:
                return "Not Found"

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    array = [51, 14, 28, 30, 97, 71, 88, 49]

    numbers_tree = build_tree(array)

    rand_searchkey = rand.choice([rand.choice(array), rand.randint(1, 100)]) # Additional

    print(numbers_tree.calculate_sum())
    print("In order traversal : ", numbers_tree.in_order_traversal())
    print("Pre order traversal : ", numbers_tree.pre_order_traversal())
    print("Post order traversal : ", numbers_tree.post_order_traversal())

    print(f"Search for : {rand_searchkey} --- ", numbers_tree.search(rand_searchkey))

    print(numbers_tree.find_max())
    print(numbers_tree.find_min())

