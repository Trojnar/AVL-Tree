from bst import BSTMap, BSTNode


class RBTNode(BSTNode):
    def __init__(self, key, value, color):
        super().__init__(key, value)
        self.color = color

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
    pass
