from __future__ import annotations
from typing import Optional


class TreeNode:
    """
    Class that represents node of Tree.

    Attributes
    ----------
    key
        Key of the node
    value
        Value assigned to given key
    left : TreeNode
        Left child node (default None)
    right : TreeNode
        Right child node (default None)
    parent : TreeNode
        Parent node.

    """

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.__key = key
        self.value = value
        self.__left = left
        self.__right = right
        self.__parent = parent

    @property
    def key(self):
        return self.__key

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def parent(self):
        return self.__parent

    @left.setter
    def left(self, new_left):
        if isinstance(new_left, TreeNode):
            self.__left = new_left
        else:
            raise Exception("Data type of the attribute left should be TreeNode().")

    @right.setter
    def right(self, new_right):
        if isinstance(new_right, TreeNode):
            self.__right = new_right
        else:
            raise Exception("Data type of the attribute right should be TreeNode().")

    @parent.setter
    def parent(self, new_parent):
        if isinstance(new_parent, TreeNode):
            self.__parent = new_parent
        else:
            raise Exception("Data type of the attribute parent should be TreeNode().")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.key}, {self.value}, {self.left}, "
            f"{self.right}, {self.parent})"
        )

    def __str__(self):
        return str(self.key)

    @staticmethod
    def __is_none(object):
        # Leaf's left/right element can be None or TreeNode(None, None)
        # this helper method identify if self is blank element or not.
        if object is None or (isinstance(object, TreeNode) and object.key == None):
            return True
        return False

    @staticmethod
    def __is_leaf(object):
        # Return True if node is leaf.
        if TreeNode.__is_none(object.left) and TreeNode.__is_none(object.right):
            return True
        return False

    def to_tuple(self) -> Optional[tuple]:
        if TreeNode.__is_none(self):
            return None

        return (
            TreeNode.to_tuple(self.left),  # type: ignore
            self.key,
            TreeNode.to_tuple(self.right),  # type: ignore
        )

    def height(self):
        if TreeNode.__is_none(self):
            return 0

        return 1 + max(
            TreeNode.height(self.left), TreeNode.height(self.right)  # type: ignore
        )

    def display_keys(self, level=0):
        if TreeNode.__is_none(self):
            print(level * "\t", "Ø")
            return

        if TreeNode.__is_leaf(self):
            print(level * "\t", self.key)
            return

        TreeNode.display_keys(self.right, level + 1)  # type: ignore
        print(level * "\t", self.key)
        TreeNode.display_keys(self.left, level + 1)  # type: ignore

    def length(self):
        if TreeNode.__is_none(self):
            return 0

        return (
            1 + TreeNode.length(self.left) + TreeNode.length(self.right)  # type: ignore
        )

    def min_depth(self):
        if TreeNode.__is_none(self):
            return 0

        return 1 + min(
            TreeNode.min_depth(self.left), TreeNode.min_depth(self.right)  # type: ignore
        )

    def traverse_inorder(self) -> list:
        # left root right
        if TreeNode.__is_none(self):
            return []

        return (
            TreeNode.traverse_inorder(self.left)  # type: ignore
            + [self.key]
            + TreeNode.traverse_inorder(self.right)  # type: ignore
        )

    def traverse_preorder(self) -> list:
        # root left rigth
        if TreeNode.__is_none(self):
            return []
        return (
            [self.key]
            + TreeNode.traverse_preorder(self.left)  # type: ignore
            + TreeNode.traverse_preorder(self.right)  # type: ignore
        )

    def traverse_postorder(self) -> list:
        # right left root
        if TreeNode.__is_none(self):
            return []

        return (
            TreeNode.traverse_postorder(self.left)  # type: ignore
            + TreeNode.traverse_postorder(self.right)  # type: ignore
            + [self.key]
        )

    def insert(self, node):
        self.__insert(node, self.min_depth())

    def __insert(self, node, min_depth, depth=1, inserted=False):
        if TreeNode.__is_none(self.left) and not inserted and depth == min_depth:
            self.left = node
            self.left.parent = self
            return True
        elif TreeNode.__is_none(self.right) and not inserted and depth == min_depth:
            self.right = node
            self.right.parent = self
            return True
        elif TreeNode.__is_leaf(self):
            return False

        inserted = TreeNode.__insert(
            self.left, node, min_depth, depth + 1, inserted  # type: ignore
        )
        if not inserted:
            inserted = TreeNode.__insert(
                self.right, node, min_depth, depth + 1, inserted  # type: ignore
            )

        if inserted:
            return True
        else:
            return False

    # def __insert(self, node, min_depth, level=1, complete=None):
    #     print(self, min_depth, level)
    #     if TreeNode.__is_none(self):
    #         # if is None it means it is blank spot somewhere in the middle of the tree,
    #         # because algorithm returns if encounters a leaf.
    #         return False

    #     if TreeNode.__is_leaf(self) and min_depth != level:
    #         # Return if node is a leaf and is higher than blank spot in the middle of
    #         # the tree.
    #         return
    #     elif TreeNode.__is_leaf(self) and min_depth == level:
    #         # Case, when leaf is parent node. No blank spots in the middle of the
    #         # tree.
    #         print(self)
    #         print("Ø")
    #         self.right
    #         return True

    #     complete = TreeNode.__insert(self.left, node, min_depth, level + 1, complete)  # type: ignore

    #     if complete == None:
    #         complete = TreeNode.__insert(self.right, node, min_depth, level + 1, complete)  # type: ignore

    #     if complete:
    #         return True


class TreeMap:
    """
    Class that provides mapping of tree nodes. Mapping begins at node provided as root
    attribute up.

    Attributes
    ----------
    root: TreeNode
        Initial node of the tree.

    Methods
    ---------
    insert(node : TreeNode)
        Inserts node to TreeMap instance's tree.
    find(key) -> TreeNode
        Returns node of given key or None if not found.
    update(key, value) -> boolean
        Returns True if updated or False if not found.
    display_keys()
        Displays tree in standard output.
    to_list()
        Returns tree converted to list format [node1, node2, ..., nodeN].
    to_tuple()
        Returns tree converted to tuple format (left_subtree, node, right_subtree).
    traverse_preorder() -> list
        Traverse tree preorder. Returns list.
    traverse_inorder() -> list
        Traverse tree inorder. Returns list.
    traverse_postorder() -> list
        Traverse tree postorder. Returns list.
    is_complete() -> boolean
        Checks if tree is complete.
    height() -> int
        Returns tree height.
    len() -> int
        Returns tree length.


    """

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, key, value):
        """
        Allows to insert node to the tree. Node is added to the first available place
        from the left.

        Parameters
        ----------
        node
            Node to insert.
        """
        node = TreeNode(key, value)
        self.root.insert(node)

    def find(self, key) -> TreeNode:
        """
        Finds node of given key.

        Parameters
        ----------
        key
            Key of wanted node.

        Returns
        -------
        TreeNode
            Node of given key or None if not found.
        """
        pass

    def update(self, key, value) -> bool:
        """
        Updates node.

        Parameters
        ----------
        key
            Key of the node to update
        value
            Value to update.
        """
        pass

    def display_keys(self, root=None, level=0):
        """Displays keys in tree-like form at stdout."""
        self.root.display_keys()

    def to_tuple(self) -> Optional[tuple]:
        """
        Returns
        -------
        tuple
            Tuple organized in form of (left_subtree, key, right_subtree)
        """
        return self.root.to_tuple()

    @classmethod
    def parse_tuple(cls, tree_t: tuple) -> TreeMap:
        """
        Parse given tuple organized in form (left_subtree, root, right_subtree).

        Parameters
        ----------
        tree : tuple
            tuple of key-value paris of the tree organized in form of
            (left_subtree, key-value, right_subtree).

        Returns
        --------
        TreeMap
            Map of the tree created from tuple.
        """

        return cls(cls.__create_tree_from_tuple(tree_t))

    @staticmethod
    def __create_tree_from_tuple(tree_t: tuple):
        """Creates tree from tuple and returns root node."""
        if tree_t is None:
            return TreeNode(None, None)
        tree_node = TreeNode(tree_t[1], tree_t[1])
        tree_node.left = TreeMap.__create_tree_from_tuple(tree_t[0])
        tree_node.left.parent = tree_node
        tree_node.right = TreeMap.__create_tree_from_tuple(tree_t[2])
        tree_node.right.parent = tree_node
        return tree_node

    def traverse_preorder(self) -> list:
        """
        Traverse tree preorder. Returns list.

        Returns
        --------
        list
            List of nodes in preorder.

        """
        return self.root.traverse_preorder()

    def traverse_postorder(self) -> list:
        """
        Traverse tree post. Returns list.

        Returns
        --------
        list
            List of nodes postorder.
        """
        return self.root.traverse_postorder()

    def traverse_inorder(self) -> list:
        """
        Traverse tree post. Returns list.

        Returns
        --------
        list
            List of nodes inorder.

        """
        return self.root.traverse_inorder()

    def is_complete(self) -> bool:
        """
        Checks if tree is complete

        Returns
        --------
        boolean
            True if tree is complete, False if not
        """
        return True

    def height(self) -> int:
        """
        Returns
        -------
        int
            Height/depth of the tree.
        """
        return self.root.height()

    def length(self) -> int:
        """
        Returns
        -------
        int
            Amount of the elements in the tree.
        """
        return self.root.length()

    def min_depth(self) -> int:
        """
        Returns
        -------
        int
            Minimal height/depth of the tree.
        """
        return self.root.min_depth()
