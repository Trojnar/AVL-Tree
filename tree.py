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
        self._left = None
        self._right = None
        self._parent = None

    @property
    def key(self):
        return self.__key

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent

    @left.setter
    def left(self, new_left):
        if isinstance(new_left, TreeNode):
            self._left = new_left
        else:
            raise Exception("Attribute left should be of type TreeNode.")

    @right.setter
    def right(self, new_right):
        if isinstance(new_right, TreeNode):
            self._right = new_right
        else:
            raise Exception("Attribute right should be of type TreeNode.")

    @parent.setter
    def parent(self, new_parent):
        if isinstance(new_parent, TreeNode):
            self._parent = new_parent
        else:
            raise Exception("Attribute parent should be of type TreeNode.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.value})"

    def __str__(self):
        return str(self.key)

    @staticmethod
    def _is_none(object):
        # Leaf's left/right element can be None or TreeNode(None, None)
        # this helper method identify if self is blank element or not.
        if object is None or (isinstance(object, TreeNode) and object.key == None):
            return True
        return False

    @staticmethod
    def _is_leaf(object):
        # Return True if node is a leaf.
        if TreeNode._is_none(object.left) and TreeNode._is_none(object.right):
            return True
        return False

    def to_tuple(self) -> tuple:
        """
        Returns
        -------
        tuple
            Tuple of keys in (left-subtree, key, right-subtree) order.
        """
        if TreeNode._is_none(self):
            return None  # type: ignore

        return (
            TreeNode.to_tuple(self.left),  # type: ignore
            self.key,
            TreeNode.to_tuple(self.right),  # type: ignore
        )

    def height(self):
        # BUG: Counting of height should start from 0, so for now real height is
        # self.height()-1
        if TreeNode._is_none(self):
            return -1

        return 1 + max(
            TreeNode.height(self.left), TreeNode.height(self.right)  # type: ignore
        )

    def display_keys(self, level=0):
        if TreeNode._is_none(self):
            print(level * "\t", "Ø")
            return

        if TreeNode._is_leaf(self):
            print(level * "\t", self.key)
            return

        TreeNode.display_keys(self.right, level + 1)  # type: ignore
        print(level * "\t", self.key)
        TreeNode.display_keys(self.left, level + 1)  # type: ignore

    def length(self):
        if TreeNode._is_none(self):
            return 0

        return (
            1 + TreeNode.length(self.left) + TreeNode.length(self.right)  # type: ignore
        )

    def min_depth(self):
        if TreeNode._is_none(self):
            return 0

        return 1 + min(
            TreeNode.min_depth(self.left), TreeNode.min_depth(self.right)  # type: ignore
        )

    def traverse_inorder(self) -> list:
        # left root right
        if TreeNode._is_none(self):
            return []

        return (
            TreeNode.traverse_inorder(self.left)  # type: ignore
            + [self]
            + TreeNode.traverse_inorder(self.right)  # type: ignore
        )

    def max_left(self):
        if TreeNode._is_none(self.left):
            return self

        return TreeNode.max_left(self.left)

    def max_right(self):
        if TreeNode._is_none(self.right):
            return self

        return TreeNode.max_right(self.right)

    def inorder_successor(self, f_next=False):
        # Inorder successor will be first node to return when traverse right subtree
        # (max left of the right subtree or right itself).
        if not TreeNode._is_none(self.right):
            return self.right.max_left()

    def inorder_predecessor(self):
        # Inorder predecessor will be last node if traverse left subtree.
        # (max right of the left subtree or left itself).
        if not TreeNode._is_none(self.left):
            return self.left.max_right()
        elif not TreeNode._is_none(self.parent):
            return self.parent
        else:
            return None

    def traverse_preorder(self) -> list:
        # root left right
        if TreeNode._is_none(self):
            return []
        return (
            [self]
            + TreeNode.traverse_preorder(self.left)  # type: ignore
            + TreeNode.traverse_preorder(self.right)  # type: ignore
        )

    def traverse_postorder(self) -> list:
        # right left root
        if TreeNode._is_none(self):
            return []

        return (
            TreeNode.traverse_postorder(self.left)  # type: ignore
            + TreeNode.traverse_postorder(self.right)  # type: ignore
            + [self]
        )

    def insert(self, node):
        if TreeNode._is_none(self):
            # If root is blank node - replace instance attributes and return.
            self.__dict__ = node.__dict__
            return
        self.__insert(node, self.min_depth())

    def __insert(self, node, min_depth, depth=1, inserted=False):
        if depth > min_depth:
            # Don't look deeper than level where blank spot is.
            return False
        elif TreeNode._is_none(self.left) and not inserted:
            # If first blank spot from the left at left branch found - insert node:
            self.left = node
            self.left.parent = self
            return True
        elif TreeNode._is_none(self.right) and not inserted:
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

    def is_parent_of(self, node: TreeNode) -> Optional[bool]:
        """
        Method checks if the node is parent of given node.

        Parameters
        ----------
        node
            Node to check if it is a child.

        Returns
        -------
        bool
            True if the node is parent of given node.
        """
        if self is node:
            return True
        elif TreeNode._is_none(self.left) and TreeNode._is_none(self.right):
            return

        left = TreeNode.is_parent_of(self.left, node)  # type: ignore
        right = TreeNode.is_parent_of(self.right, node)  # type: ignore

        if left or right:
            return True
        else:
            return False

    def is_child_of(self, node: TreeNode) -> Optional[bool]:
        """
        Method checks if the node is child of given node.

        Parameters
        ----------
        node
            Node to check if it is a child.

        Returns
        -------
        bool
            True if the node is parent of given node.
        """
        if node is None:
            return False

        return node.is_parent_of(self)

    def _find_rightmost(self, max_depth, level=0, leaf=None):
        if TreeNode._is_leaf(self) and level == max_depth:
            return self
        elif TreeNode._is_leaf(self):
            return

        if leaf is None and not TreeNode._is_none(self.right):
            leaf = TreeNode._find_rightmost(self.right, max_depth, level + 1, leaf)
        if leaf is None and not TreeNode._is_none(self.left):
            leaf = TreeNode._find_rightmost(self.left, max_depth, level + 1, leaf)

        if leaf is not None:
            return leaf

    def _remove(self, rightmost):

        assert rightmost is not None
        assert not self._is_none(rightmost.parent)

        if rightmost.parent.left == rightmost:
            rightmost.parent.left = TreeNode(None, None)
        elif rightmost.parent.right == rightmost:
            rightmost.parent.right = TreeNode(None, None)

        rightmost.parent = (
            self.parent if self.parent is not None else TreeNode(None, None)
        )
        rightmost.left = self.left
        rightmost.right = self.right
        self.__dict__ = rightmost.__dict__

    def remove(self, node):
        rightmost = self._find_rightmost(max_depth=self.height())
        TreeNode._remove(node, rightmost)

    def swap_nodes(self, second):
        key = self.__key
        value = self.value
        self.__key = second.key
        self.value = second.value
        second.__key = key
        second.value = value


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
    length() -> int
        Returns tree length.


    """

    node_class = TreeNode

    def __init__(self, root: TreeNode):
        if isinstance(root, TreeNode):
            self.root = root
        else:
            raise ValueError("Root should be TreeNode instance.")
        self.node_class = TreeNode

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
        assert last != None, "last should never be None."
        return nodes_l[first[1] : last[1] + 1]

    def find_node(
        self,
        node: TreeNode,
    ) -> Optional[TreeNode]:
        """
        Finds the first occurrence of node which has the same key and value.

        Parameters
        ----------
            node : TreeNode
                Node that is searched for.

        Returns
        -------
            Optional[TreeNode]
                Node that is searched for.
        """

        if node.key == None:
            return None

        nodes_l = self.find(node.key)
        nodes_l_val = []
        if nodes_l == None:
            return None

        # make list of values with indexes if the searching for node's value is None,
        # it's changed to -1
        nodes_l_val = list(
            map(
                lambda x, y: (x.value, y) if x.value != None else (-1, y),
                nodes_l,
                range(len(nodes_l)),
            )
        )

        # sort list by value. If value is none move it to the end of the list
        nodes_l_val.sort(key=lambda x: x[0])

        values, indexes = self.__unzip_list(nodes_l_val)

        # If searching for node's value is None, change it to -1.
        value = -1 if node.value == None else node.value

        index = self.__find_first_value(values, value)

        if index == None:
            return None

        return nodes_l[indexes[index]]

    def remove(self, node: TreeNode):
        """Removes first node that have exact same key and value."""
        # Finds deepest rightmost node and replace it with the node to delete.
        n = self.find_node(node)
        if node is not None:
            self.root.remove(n)

    @staticmethod
    def __unzip_list(zipped_list):
        """Extract given list of tuples [(value1, value2), ...] to two lists
        [value1, ...], [value2, ...]"""
        first = []
        second = []
        for i, j in zipped_list:
            first.append(i)
            second.append(j)
        return first, second

    @staticmethod
    def __find_first_value(li: list[int], value) -> Optional[int]:
        """
        Finds first occurrence of value in given list of values.
        """
        lo = 0
        hi = len(li) - 1
        while hi > lo:
            mid = (hi - lo) // 2
            if li[lo + mid] == value:
                if hi > 2 and li[lo + mid - 1] == value:
                    hi -= mid
                else:
                    lo = lo + mid
                    hi = lo
                    break
            elif (hi - lo) > 1 and li[lo + mid] > value:
                hi -= mid
            elif (hi - lo) > 1 and li[lo + mid] < value:
                lo += mid + 1

        if hi == lo and li[lo] == value:
            return lo
        else:
            return None

    @staticmethod
    def __find_first_occurrence(nodes: list[TreeNode], key) -> Optional[tuple]:
        """
        Search through sorted list of nodes and find first occurrence of the given key.
        It's faster than __find_first, because there is no need to map node's keys.
        Binary search algorithm implementation was used.

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

        while hi > lo:
            mid = (hi - lo) // 2
            if nodes[lo + mid].key == key:
                if hi > 2 and nodes[lo + mid - 1].key == key:
                    hi -= mid
                else:
                    lo = lo + mid
                    hi = lo
                    break
            elif (hi - lo) > 1 and nodes[lo + mid].key > key:
                hi -= mid
            elif (hi - lo) > 1 and nodes[lo + mid].key < key:
                lo += mid + 1
            else:
                break

        if hi == lo and nodes[lo].key == key:
            return nodes[lo], lo
        else:
            return None

    @staticmethod
    def __find_last_occurrence(nodes: list[TreeNode], key) -> Optional[tuple]:
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

    def update(self, node, new_value) -> bool:
        """
        Updates value of the first occurrence of node with new value.

        Parameters
        ----------
        node
            Node to update.
        new_node
            Node to update with.
        """
        node = self.find_node(node)
        if node == None:
            return False
        node.value = new_value
        return True

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

    @classmethod
    def __create_tree_from_tuple(cls, tree_t: tuple):
        """Creates tree from tuple of keys and returns root node."""
        if tree_t is None:
            # TODO : Make Nones at the end of the tree not TreeNode(None, None)
            return cls.node_class(None, None)
        tree_node = cls.node_class(tree_t[1], None)
        tree_node.left = cls.__create_tree_from_tuple(tree_t[0])
        tree_node.left.parent = tree_node
        tree_node.right = cls.__create_tree_from_tuple(tree_t[2])
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

    @staticmethod
    def __is_full(root, last_level, level=0) -> Optional[bool]:
        """
        Returns True if there is full in the levels before the last_level inclusive.
        """
        if root == None or root.key == None:
            return False

        if level == last_level - 1:
            return True

        left = TreeMap.__is_full(root.left, last_level, level + 1)
        right = TreeMap.__is_full(root.right, last_level, level + 1)
        if left and right:
            return True
        else:
            return False

    @staticmethod
    def is_full(root: TreeNode, last_level) -> Optional[bool]:
        if isinstance(root, TreeNode):
            if last_level == 0:
                return True
            else:
                return TreeMap.__is_full(root, last_level)
        else:
            raise TypeError("Passed parameter 'root' have to be of the type TreeNode.")

    def is_complete(self) -> bool:
        """
        Checks if tree is complete

        Returns
        --------
        boolean
            True if tree is complete, False if not
        """
        if TreeMap.is_full(self.root, self.root.height()) and self.is_max_left():
            return True
        # every level before the last is full
        # every node at lowest level is as far left as possible

    @staticmethod
    def __is_max_left(root, height, level=0) -> bool:
        # True True and True False == True
        # TODO: some static methods - like this one for example should be in class
        # TreeNode. and here should be method that uses that method for
        # attribute height and root of TreeMap.
        if root == None or root.key == None:
            return False

        if level == height:
            return True

        left = TreeMap.__is_max_left(root.left, height, level + 1)
        right = TreeMap.__is_max_left(root.right, height, level + 1)

        if (left and right) or (left and not right):
            return True
        else:
            return False

    def is_max_left(self):
        return TreeMap.__is_max_left(self.root, self.height())

    def height(self) -> int:
        """
        Returns
        -------
        int
            Height/depth of the tree.
        """
        # TODO create attribute height, length and min depth
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

    def __eq__(self, other_node: TreeMap) -> bool:
        """
        Method checks if TreeMaps are the same.
        """
        if not isinstance(other_node, TreeMap):
            return NotImplemented

        return TreeMap.subtrees_eq(self.root, other_node.root)

    @staticmethod
    def subtrees_eq(root: Optional[TreeNode], other: Optional[TreeNode]) -> bool:
        """
        Method checks if subtrees starting from the root down are the same.

        Parameters
        ----------
        root : Optional[TreeNode]
            Root of the subtree to check.
        other : Optional[TreeNode]
            Root of the subtree to compare with.

        Returns
        -------
        bool
            returns True if subtrees are the same, otherwise returns False.

        """
        # Handling Nones
        if (type(root) == type(None) and type(other) != type(None)) or (
            type(root) != type(None) and type(other) == type(None)
        ):  # TODO XOR !=
            return False
        elif type(root) == type(None) and type(other) == type(None):
            return True
        elif root != other:
            return False

        left = TreeMap.subtrees_eq(root.left, other.left)  # type: ignore
        right = TreeMap.subtrees_eq(root.right, other.right)  # type: ignore

        if left and right:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return str(self.to_tuple())
