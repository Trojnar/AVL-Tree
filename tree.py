from __future__ import annotations
from typing import Iterable, Optional, Union


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

    def __init__(self, key, value):
        self.__key = key
        self.value = value
        self.__left = None
        self.__right = None
        self.__parent = None

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
            raise Exception("Attribute left should be of type TreeNode.")

    @right.setter
    def right(self, new_right):
        if isinstance(new_right, TreeNode):
            self.__right = new_right
        else:
            raise Exception("Attribute right should be of type TreeNode.")

    @parent.setter
    def parent(self, new_parent):
        if isinstance(new_parent, TreeNode):
            self.__parent = new_parent
        else:
            raise Exception("Attribute parent should be of type TreeNode.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.value})"

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

    def to_tuple(self) -> tuple:
        """
        Returns
        -------
        tuple
            Tuple of keys in (left-subtree, key, right-subtree) order.
        """
        if TreeNode.__is_none(self):
            return None  # type: ignore

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
            + [self]
            + TreeNode.traverse_inorder(self.right)  # type: ignore
        )

    def traverse_preorder(self) -> list:
        # root left rigth
        if TreeNode.__is_none(self):
            return []
        return (
            [self]
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
            + [self]
        )

    def insert(self, node):
        if TreeNode.__is_none(self):
            # If root is blank node - replace instance attributes and return.
            self.__dict__ = node.__dict__
            return
        self.__insert(node, self.min_depth())

    def __insert(self, node, min_depth, depth=1, inserted=False):
        if depth > min_depth:
            # Don't look deeper than level where blank spot is.
            return False
        elif TreeNode.__is_none(self.left) and not inserted:
            # If first blank spot from the left at left branch found - insert node:
            self.left = node
            self.left.parent = self
            return True
        elif TreeNode.__is_none(self.right) and not inserted:
            # If first blank spot from the left at right branch found - insert node:
            self.right = node
            self.right.parent = self
            return True

        inserted = TreeNode.__insert(
            self.left, node, min_depth, depth + 1, inserted  # type: ignore
        )
        if not inserted:
            # if node already inserted, don't look further.
            inserted = TreeNode.__insert(
                self.right, node, min_depth, depth + 1, inserted  # type: ignore
            )

        if inserted:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        If key and value are the same for self and other, node is considered equal.
        """
        if not isinstance(other, TreeNode):
            if type(self) == None and type(other) == None:
                return True
            elif (type(self) == None and type(other) != None) or (
                type(self) != None and type(other) == None
            ):
                return False
            else:
                return NotImplemented

        return self.key == other.key and self.value == other.value

    def is_free(self):
        """
        Check if node is assigned to any tree.

        Returns
        -------
        bool
            If node is assigned to tree return False else return True.
        """
        if self.parent or self.right or self.left:
            return False
        return True


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
        Allows to insert key, value to the tree as node. Node is added to the first
        available place from the left. Always creates new TreeNode.

        Parameters
        ----------
        key
            Key of the node.
        value
            Value of the node.
        """
        node = TreeNode(key, value)
        self.root.insert(node)

    def insert_node(self, node: TreeNode):
        """
        Allows to insert node to the tree. Node is added to the first free branch from
        the left. Creates new node only if given node is already bound.

        Parameters
        ----------
        node : TreeNode
            Node to insert.
        """
        if isinstance(node, TreeNode):
            if node.is_free():
                self.root.insert(node)
            else:
                self.root.insert(TreeNode(node.key, node.value))
        else:
            return False

    def to_list(self):
        """
        Returns list of nodes sorted by key.

        Returns
        -------
        list
            List of nodes sorted by key.

        """

        nodes = self.root.traverse_inorder()
        nodes.sort(key=lambda x: x.key)
        return nodes

    def parse_list(self, nodes_l: Union[list[TreeNode], list[tuple], list[list]]):
        """
        Parse given list placing every next node of the list in first from left
        possible spot.

        Parameters
        ----------
        nodes_l : Union[list[TreeNode], list[tuple], list[list]]
            list of TreeNode instances or list of key-value pair iterable where the
            first index is key and second is value.
        """
        if isinstance(nodes_l[0], TreeNode):
            for node in nodes_l:
                self.insert(node.key, node.value)  # type: ignore
        elif isinstance(nodes_l[0], list) or isinstance(nodes_l[0], tuple):
            for node in nodes_l:
                self.insert(node[0], node[1])  # type: ignore

    def find(self, key) -> Optional[list]:
        """
        Finds the nodes of given key.

        Parameters
        ----------
        key
            Key of the wanted node.

        Returns
        -------
        list[TreeNode]
            list of the found nodes.
        """
        nodes_l = self.to_list()
        first = self.__find_first_occurrence(self.to_list(), key)
        if first == None:
            # if the node of given key not found
            return None
        last = self.__find_last_occurrence(self.to_list(), key)
        return nodes_l[first[1] : last[1] + 1]  # type: ignore

    def find_node(
        self,
        node,
    ) -> Optional[TreeNode]:
        """
        Finds the same node as given node.
        """
        pass

    @staticmethod
    def __find_first_occurrence(nodes: list[TreeNode], key, lo=0) -> Optional[tuple]:
        """
        Search through sorted list of nodes and find first occurrence of the given key.

        Parameters
        ----------
        nodes : list
            List of sorted nodes to search in.
        key
            Key of wanted node

        Returns
        -------
        tuple
            (last_node, index of the first node)

        """
        lo = 0
        hi = len(nodes) - 1

        while hi > lo + 1:
            mid = (hi - lo) // 2
            if nodes[lo + mid].key == key:
                if nodes[lo + mid - 1].key == key:
                    hi -= mid
                else:
                    lo = lo + mid
                    hi = lo
                    break
            elif nodes[lo + mid].key > key:
                hi -= mid
            elif nodes[lo + mid].key < key:
                lo += mid

        if hi == lo and nodes[lo].key == key:
            return nodes[lo], lo
        else:
            return None

    @staticmethod
    def __find_last_occurrence(nodes: list[TreeNode], key, lo=0) -> Optional[tuple]:
        """
        Search through sorted list of nodes and find last occurrence of the given key.

        Parameters
        ----------
        nodes : list
            List of sorted nodes to search in.
        key
            Key of wanted node.

        Returns
        -------
        tuple
            (last node, index of the last node)

        """
        lo = 0
        hi = len(nodes) - 1

        while hi >= lo + 1:
            mid = (hi - lo) // 2

            if nodes[lo + mid].key == key:
                if nodes[lo + mid + 1].key == key:
                    lo += mid + 1
                else:
                    lo = lo + mid
                    hi = lo
                    break
            elif nodes[lo + mid].key > key:
                hi -= mid
            elif nodes[lo + mid].key < key:
                lo += mid

        if hi == lo and nodes[lo].key == key:
            return nodes[lo], lo
        else:
            return None

    def update(self, node1, node2) -> bool:
        """
        Updates the node.

        Parameters
        ----------
        node1
            Node to update.
        node2
            Node to update with.
        """
        pass

    def display_keys(self, root=None, level=0):
        """Displays the keys in tree-like form at stdout."""
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
        Parse given tuple of keys organized in form (left_subtree, root, right_subtree).

        Parameters
        ----------
        tree : tuple
            tuple of keys of the tree organized in form of
            (left_subtree, key, right_subtree).

        Returns
        --------
        TreeMap
            Map of the tree created from tuple.
        """

        return cls(cls.__create_tree_from_tuple(tree_t))

    @staticmethod
    def __create_tree_from_tuple(tree_t: tuple):
        """Creates tree from tuple of keys and returns root node."""
        if tree_t is None:
            # TODO : Make Nones at the end of the tree not TreeNode(None, None)
            return TreeNode(None, None)
        tree_node = TreeNode(tree_t[1], None)
        tree_node.left = TreeMap.__create_tree_from_tuple(tree_t[0])
        tree_node.left.parent = tree_node
        tree_node.right = TreeMap.__create_tree_from_tuple(tree_t[2])
        tree_node.right.parent = tree_node
        return tree_node

    def traverse_preorder(self) -> list:
        """No
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

    def subtrees_eq(self, other):
        # TODO
        """
        Method checks if subtrees starting from root down are the same.
        """
        if (type(self) == type(None) and type(other) != type(None)) or (
            type(self) != type(None) and type(other) == type(None)
        ):
            return False
        elif type(self) == type(None) and type(other) == type(None):
            return True

        if not isinstance(other, TreeNode):
            return NotImplemented

        return (
            self.key == other.key
            and self.value == other.value
            and self.left == other.left
            and self.right == other.right
        )

    def is_child(self, child, other):
        # TODO
        """
        Method checks node is child of other node.
        """
        if (type(self) == type(None) and type(other) != type(None)) or (
            type(self) != type(None) and type(other) == type(None)
        ):
            return False
        elif type(self) == type(None) and type(other) == type(None):
            return True

        if not isinstance(other, TreeNode):
            return NotImplemented

        return self.key == other.key and self.value == other.value and self.parent

    def __repr__(self) -> str:
        return str(self.to_tuple())
