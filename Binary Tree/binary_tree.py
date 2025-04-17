class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_element(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    else:
                        current = current.right

    def search_element(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete_element(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def minimum_value(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def maximum_value(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    # In-order traversal
    def inorder(self):
        return ' '.join(self._inorder_recursive(self.root))

    def _inorder_recursive(self, node):
        if node is None:
            return []
        return self._inorder_recursive(node.left) + [str(node.value)] + self._inorder_recursive(node.right)

    # Pre-order traversal
    def preorder(self):
        return ' '.join(self._preorder_recursive(self.root))

    def _preorder_recursive(self, node):
        if node is None:
            return []
        return [str(node.value)] + self._preorder_recursive(node.left) + self._preorder_recursive(node.right)

    # Post-order traversal
    def postorder(self):
        return ' '.join(self._postorder_recursive(self.root))

    def _postorder_recursive(self, node):
        if node is None:
            return []
        return self._postorder_recursive(node.left) + self._postorder_recursive(node.right) + [str(node.value)]

# Example usage
if __name__ == "__main__":
    # Step 1: Create a binary tree with root value 10
    bt = BinaryTree(10)
    print("Initial tree (in-order):", bt.inorder())  # 10

    # Step 2: Insert elements
    bt.insert_element(5)
    bt.insert_element(15)
    bt.insert_element(2)
    bt.insert_element(7)
    bt.insert_element(12)
    bt.insert_element(20)

    # Step 3: Display tree using all traversals
    print("\nTree after insertions:")
    print("In-order   :", bt.inorder())     # 2 5 7 10 12 15 20
    print("Pre-order  :", bt.preorder())    # 10 5 2 7 15 12 20
    print("Post-order :", bt.postorder())   # 2 7 5 12 20 15 10

    # Step 4: Search for elements
    print("\nSearching elements:")
    print("Search for 7  :", bt.search_element(7))    # True
    print("Search for 100:", bt.search_element(100))  # False

    # Step 5: Display minimum and maximum values
    print("\nTree boundaries:")
    print("Minimum value:", bt.minimum_value())  # 2
    print("Maximum value:", bt.maximum_value())  # 20

    # Step 6: Delete a node with two children (5)
    bt.delete_element(5)
    print("\nAfter deleting 5 (node with two children):")
    print("In-order   :", bt.inorder())     # 2 7 10 12 15 20
    print("Pre-order  :", bt.preorder())    # 10 7 2 15 12 20
    print("Post-order :", bt.postorder())   # 2 7 12 20 15 10

    # Step 7: Delete a leaf node (20)
    bt.delete_element(20)
    print("\nAfter deleting 20 (leaf node):")
    print("In-order   :", bt.inorder())     # 2 7 10 12 15
    print("Pre-order  :", bt.preorder())    # 10 7 2 15 12
    print("Post-order :", bt.postorder())   # 2 7 12 15 10

    # Step 8: Delete root node (10)
    bt.delete_element(10)
    print("\nAfter deleting 10 (root node):")
    print("In-order   :", bt.inorder())     # 2 7 12 15
    print("Pre-order  :", bt.preorder())    # 12 7 2 15
    print("Post-order :", bt.postorder())   # 2 7 15 12
