from tree import TreeNode, TreeMap


class BSTNode(TreeNode):
    """Binary search tree node."""

    def find(self, key):
        if self.key == key:
            return self
        elif BSTNode._is_leaf(self):
            return

        if not BSTNode._is_none(self.left) and key < self.key:
            return BSTNode.find(self.left, key)
        if not BSTNode._is_none(self.right) and key > self.key:
            return BSTNode.find(self.right, key)

    def insert(self, key, value):
        if BSTNode._is_none(self):
            return True

        if key > self.key:
            r = BSTNode.insert(self.right, key, value)
            if r:
                self.right = BSTNode(key, value)
                self.right.parent = self
                return
        elif key < self.key:
            r = BSTNode.insert(self.left, key, value)
            if r:
                self.left = BSTNode(key, value)
                self.left.parent = self
                return
        elif key == key:
            print("Keys can't repeat.")
            return False


class BSTMap(TreeMap):
    """Binary search tree map"""

    node_class = BSTNode

    def __init__(self, root: BSTNode):
        if isinstance(root, BSTNode):
            self.root = root
        else:
            raise ValueError("Root should be BSTNode instance.")

    def find(self, key):
        return self.root.find(key)

    def insert(self, key, value):
        self.root.insert(key, value)

    def insert_node(self, node: BSTNode):
        self.root.insert(node.key, node.value)
