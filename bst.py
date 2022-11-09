from __future__ import annotations
from typing import Union
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

    def is_bst(self, p_key=None, side=""):
        """ """
        l, r = True, True
        if BSTNode._is_none(self):
            return True
        elif side == "l" and self.key >= p_key:
            return False
        elif side == "r" and self.key <= p_key:
            return False

        if not BSTNode._is_none(self.left):
            l = BSTNode.is_bst(self.left, self.key, "l")
        elif not BSTNode._is_none(self.right):
            r = BSTNode.is_bst(self.right, self.key, "r")

        if l and r:
            return True
        else:
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

    def remove(self, key):
        """Removes node of given key."""
        pass

    def is_bst(self):
        return self.root.is_bst()

    @classmethod
    def parse_tuple(cls, tree_t) -> BSTMap:
        """Creates tree from given tuple. Tuple's elements are tree's keys."""
        tree = super().parse_tuple(tree_t)
        if tree.is_bst():
            return tree
        else:
            raise ValueError("Passed tuple is not binary search tree.")
            del tree
            return False

    @classmethod
    def parse_list(cls, nodes_l: Union[list[TreeNode], list[tuple], list[list]]):
        """Parses a list to bst tree, elements of the list are inserted in sequence"""
        if isinstance(nodes_l, list) and len(nodes_l) > 0:
            if isinstance(nodes_l[0], BSTNode):
                # elements are of the type BSTNode.
                root = nodes_l[0]
                tree = BSTMap(root)

                for node in nodes_l:
                    tree.insert_node(node)

                return tree
            elif isinstance(nodes_l[0], tuple) or isinstance(nodes_l[0], list):
                # elements are of the type tuple (key, value).
                root = BSTNode(nodes_l[0][0], nodes_l[0][1])
                tree = BSTMap(root)
                for node in nodes_l:
                    tree.insert(node[0], node[1])
                return tree
            elif isinstance(nodes_l[0], list):
                # elements are of the type list [key, value].
                pass
            else:
                raise TypeError("Type of the elements in the list is not supported.")
        else:
            raise TypeError("Argument node_l have to be of the type list.")
