from bst import BSTMap, BSTNode
from tree import TreeNode


class RBTNode(BSTNode):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.color = "black"
        self.left = None
        self.right = None

    @TreeNode.left.setter
    def left(self, new_left):
        if self.key is not None and new_left is None:
            # None values in leafs will be RBTNode(None, None) which gives them a color.
            new_left = RBTNode(None, None)
            self._left = new_left
        elif isinstance(new_left, TreeNode):
            self._left = new_left
        elif new_left is None:
            self._left = None
        else:
            raise TypeError(
                "value passed as left attribute should be of the type None or RBTNode"
            )

    @TreeNode.right.setter
    def right(self, new_right):
        if self.key is not None and new_right is None:
            # None values in leafs will always be RBTNode(None, None) which gives them
            # a color.
            self._right = RBTNode(None, None)
        elif isinstance(new_right, TreeNode):
            self._right = new_right
        elif new_right is None:
            self._right = None
        else:
            raise TypeError(
                "value passed as left attribute should be of the type None or RBTNode"
            )

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        if isinstance(new_color, str):
            new_color = new_color.lower()
            if new_color == "black" or new_color == "red":
                self.__color = new_color
            else:
                raise ValueError("Argument 'color' have to be either 'red' or 'black.")
        else:
            raise TypeError("Argument 'color', have to be of the type str.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.key}, {self.value}, {self.color})"


class RBTMap(BSTMap):
    """Implementation of self-balancing red-black tree."""

    node_class = RBTNode

    def insert(self):
        pass
