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
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    array = [51, 14, 28, 30, 97, 71, 88, 49]

    numbers_tree = build_tree(array)

    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(97))