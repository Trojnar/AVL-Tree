# type: ignore

from unittest import TestCase
import unittest
from tree import TreeMap
from tree import TreeNode


class TestTreeMap(TestCase):
    def setUp(self):
        test_cases = [
            # 0
            (
                ((None, 2, None), 7, (None, 6, None)),
                1,
                (None, 9, ((None, 5, None), 9, None)),
            ),
            # 1
            (None, 1, (None, 2, (None, 3, (None, 4, None)))),
            # 2
            ((((None, 4, None), 3, None), 2, None), 1, None),
            # 3
            (
                (
                    ((None, 4, None), 10, (None, 12, None)),
                    15,
                    ((None, 18, None), 22, (None, 24, None)),
                ),
                25,
                (
                    ((None, 31, None), 25, (None, 44, None)),
                    50,
                    ((None, 66, None), 70, (None, 90, None)),
                ),
            ),
            # 4
            (
                ((None, 4, None), 2, (None, 5, None)),
                1,
                ((None, 6, None), 3, (None, 7, None)),
            ),
            # 5
            (None, 1, None),
            # 6
            (
                (
                    (
                        ((None, 6, None), 2, (None, 10, None)),
                        7,
                        ((None, 11, None), 5, (None, 12, None)),
                    ),
                    1,
                    (
                        ((None, 19, None), 5, (None, 20, None)),
                        9,
                        ((None, 5, None), 9, None),
                    ),
                )
            ),
            # 7
            (
                ((None, 2, None), 7, None),
                1,
                ((None, 5, None), 9, ((None, 5, None), 9, None)),
            ),
            # 8,
            (
                ((None, 2, None), 7, None),
                1,
                ((None, 5, None), 9, ((None, 5, None), 9, None)),
            ),
        ]
        self._set_treemaps(test_cases)

    def _set_treemaps(self, test_cases):
        self.tree_maps = {
            "tree_map": TreeMap.parse_tuple(test_cases[0]),
            "only_right_tree_map": TreeMap.parse_tuple(test_cases[1]),
            "only_left_tree_map": TreeMap.parse_tuple(test_cases[2]),
            "balanced_binary_tree_4_levels_height": TreeMap.parse_tuple(test_cases[3]),
            "balanced_binary_tree_3_levels_height": TreeMap.parse_tuple(test_cases[4]),
            "one_node_tree": TreeMap.parse_tuple(test_cases[5]),
            "tree_map_last_blank": TreeMap.parse_tuple(test_cases[6]),
            "5_level_tree_map_with_blank_at_3rd_level_left": TreeMap.parse_tuple(
                test_cases[7]
            ),
            "5_level_tree_map_with_blank_at_3rd_level_right": TreeMap.parse_tuple(
                test_cases[8]
            ),
        }

    def _display_test_cases(self):
        # Helper method for debugging
        for key, tree_map in self.tree_maps:
            print(key)
            tree_map.display_keys()
            print()

    def test_create_tree_map_from_tuple(self):
        self.assertEqual(self.tree_maps["tree_map"].root.key, 1)
        self.assertEqual(self.tree_maps["tree_map"].root.parent, None)
        self.assertEqual(self.tree_maps["tree_map"].root.left.key, 7)
        self.assertEqual(
            self.tree_maps["tree_map"].root.left.parent, self.tree_maps["tree_map"].root
        )
        self.assertEqual(self.tree_maps["tree_map"].root.right.key, 9)
        self.assertEqual(
            self.tree_maps["tree_map"].root.right.parent,
            self.tree_maps["tree_map"].root,
        )
        self.assertEqual(self.tree_maps["tree_map"].root.left.left.key, 2)
        self.assertEqual(
            self.tree_maps["tree_map"].root.left.left.parent,
            self.tree_maps["tree_map"].root.left,
        )
        self.assertEqual(self.tree_maps["tree_map"].root.left.right.key, 6)
        self.assertEqual(
            self.tree_maps["tree_map"].root.left.right.parent,
            self.tree_maps["tree_map"].root.left,
        )
        self.assertEqual(self.tree_maps["tree_map"].root.right.right.key, 9)
        self.assertEqual(
            self.tree_maps["tree_map"].root.right.right.parent,
            self.tree_maps["tree_map"].root.right,
        )
        self.assertEqual(self.tree_maps["tree_map"].root.right.left.key, None)
        self.assertEqual(
            self.tree_maps["tree_map"].root.right.left.parent,
            self.tree_maps["tree_map"].root.right,
        )

        self.assertEqual(self.tree_maps["only_right_tree_map"].root.key, 1)
        self.assertEqual(self.tree_maps["only_right_tree_map"].root.left.key, None)
        self.assertEqual(self.tree_maps["only_right_tree_map"].root.right.key, 2)
        self.assertEqual(self.tree_maps["only_right_tree_map"].root.right.right.key, 3)
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.right.right.right.key, 4
        )
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.right.right.right.right.key, None
        )
        # parents
        self.assertEqual(self.tree_maps["tree_map"].root.parent, None)
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.right.parent,
            self.tree_maps["only_right_tree_map"].root,
        )
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.right.right.parent,
            self.tree_maps["only_right_tree_map"].root.right,
        )
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.right.right.right.parent,
            self.tree_maps["only_right_tree_map"].root.right.right,
        )
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.right.right.right.right.parent,
            self.tree_maps["only_right_tree_map"].root.right.right.right,
        )

        self.assertEqual(self.tree_maps["only_left_tree_map"].root.key, 1)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.right.key, None)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.left.key, 2)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.left.left.key, 3)
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.left.left.key, 4
        )
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.left.left.left.key, None
        )
        # parents
        self.assertEqual(self.tree_maps["tree_map"].root.parent, None)
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.right.parent,
            self.tree_maps["only_left_tree_map"].root,
        )
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.parent,
            self.tree_maps["only_left_tree_map"].root,
        )
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.left.parent,
            self.tree_maps["only_left_tree_map"].root.left,
        )
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.left.left.parent,
            self.tree_maps["only_left_tree_map"].root.left.left,
        )
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.left.left.left.parent,
            self.tree_maps["only_left_tree_map"].root.left.left.left,
        )

    def test_to_tuple_method(self):

        self.assertEqual(
            self.tree_maps["tree_map"].to_tuple(),
            (
                ((None, 2, None), 7, (None, 6, None)),
                1,
                (None, 9, ((None, 5, None), 9, None)),
            ),
        )
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].to_tuple(),
            (None, 1, (None, 2, (None, 3, (None, 4, None)))),
        )
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].to_tuple(),
            ((((None, 4, None), 3, None), 2, None), 1, None),
        )

    def test_height_method(self):
        self.assertEqual(self.tree_maps["tree_map"].height(), 4)
        self.assertEqual(self.tree_maps["only_right_tree_map"].height(), 4)
        self.assertEqual(self.tree_maps["only_left_tree_map"].height(), 4)

    def test_length_method(self):
        self.assertEqual(self.tree_maps["tree_map"].length(), 7)
        self.assertEqual(self.tree_maps["only_right_tree_map"].length(), 4)
        self.assertEqual(self.tree_maps["only_left_tree_map"].length(), 4)

    def test_min_depth_method(self):
        self.assertEqual(self.tree_maps["tree_map"].min_depth(), 2)
        self.assertEqual(self.tree_maps["only_right_tree_map"].min_depth(), 1)
        self.assertEqual(self.tree_maps["only_left_tree_map"].min_depth(), 1)

    def test_traverse_inorder(self):
        keys = list(
            map(
                lambda x: x.key,
                self.tree_maps[
                    "balanced_binary_tree_4_levels_height"
                ].traverse_inorder(),
            )
        )
        self.assertEqual(
            keys,
            [4, 10, 12, 15, 18, 22, 24, 25, 31, 25, 44, 50, 66, 70, 90],
        )
        keys = list(
            map(
                lambda x: x.key,
                self.tree_maps[
                    "balanced_binary_tree_3_levels_height"
                ].traverse_inorder(),
            )
        )
        self.assertEqual(
            keys,
            [4, 2, 5, 1, 6, 3, 7],
        )

    def test_traverse_preorder(self):
        keys = list(
            map(
                lambda x: x.key,
                self.tree_maps[
                    "balanced_binary_tree_4_levels_height"
                ].traverse_preorder(),
            )
        )
        self.assertEqual(
            keys,
            [25, 15, 10, 4, 12, 22, 18, 24, 50, 25, 31, 44, 70, 66, 90],
        )
        keys = list(
            map(
                lambda x: x.key,
                self.tree_maps[
                    "balanced_binary_tree_3_levels_height"
                ].traverse_preorder(),
            )
        )
        self.assertEqual(
            keys,
            [1, 2, 4, 5, 3, 6, 7],
        )

    def test_traverse_postorder(self):
        keys = list(
            map(
                lambda x: x.key,
                self.tree_maps[
                    "balanced_binary_tree_4_levels_height"
                ].traverse_postorder(),
            )
        )
        self.assertEqual(
            keys,
            [4, 12, 10, 18, 24, 22, 15, 31, 44, 25, 66, 90, 70, 50, 25],
        )
        keys = list(
            map(
                lambda x: x.key,
                self.tree_maps[
                    "balanced_binary_tree_3_levels_height"
                ].traverse_postorder(),
            )
        )
        self.assertEqual(
            keys,
            [4, 5, 2, 6, 7, 3, 1],
        )

    def test_insert_method(self):
        # blank on the left at 3rd level in 5 level tree
        self.tree_maps["tree_map"].insert(1, None)
        self.assertEqual(self.tree_maps["tree_map"].root.right.left.key, 1)
        self.assertEqual(self.tree_maps["tree_map"].root.right.left.parent.key, 9)
        self.tree_maps["tree_map"].insert(3, None)
        self.assertEqual(self.tree_maps["tree_map"].root.left.left.left.key, 3)
        self.assertEqual(self.tree_maps["tree_map"].root.left.left.left.parent.key, 2)
        self.tree_maps["tree_map"].insert(8, None)
        self.assertEqual(self.tree_maps["tree_map"].root.left.left.right.key, 8)
        self.assertEqual(self.tree_maps["tree_map"].root.left.left.right.parent.key, 2)

        # Blank on the right at 3rd level in 5 level tree

        self.tree_maps["5_level_tree_map_with_blank_at_3rd_level_right"].insert(2, 2)
        self.assertEqual(
            self.tree_maps[
                "5_level_tree_map_with_blank_at_3rd_level_right"
            ].root.left.right.key,
            2,
        )

        # Blank last one at 5th level
        self.tree_maps["tree_map_last_blank"].insert(3, None)
        self.assertEqual(
            self.tree_maps["tree_map_last_blank"].root.right.right.right.key, 3
        )
        self.assertEqual(
            self.tree_maps["tree_map_last_blank"].root.right.right.right.parent.key, 9
        )

        # one node tree
        self.tree_maps["one_node_tree"].insert(2, None)
        self.tree_maps["one_node_tree"].insert(3, None)
        self.assertEqual(self.tree_maps["one_node_tree"].root.left.key, 2)
        self.assertEqual(self.tree_maps["one_node_tree"].root.left.parent.key, 1)
        self.assertEqual(self.tree_maps["one_node_tree"].root.right.key, 3)
        self.assertEqual(self.tree_maps["one_node_tree"].root.right.parent.key, 1)

        # Only right tree
        self.tree_maps["only_left_tree_map"].insert(5, None)
        self.tree_maps["only_left_tree_map"].insert(6, 8)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.right.key, 5)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.right.parent.key, 1)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.left.right.key, 6)
        self.assertEqual(self.tree_maps["only_left_tree_map"].root.left.right.value, 8)
        self.assertEqual(
            self.tree_maps["only_left_tree_map"].root.left.right.parent.key, 2
        )

        # Only left tree
        self.tree_maps["only_right_tree_map"].insert(7, None)
        self.tree_maps["only_right_tree_map"].insert(8, None)
        self.assertEqual(self.tree_maps["only_right_tree_map"].root.left.key, 7)
        self.assertEqual(self.tree_maps["only_right_tree_map"].root.left.parent.key, 1)
        self.assertEqual(self.tree_maps["only_right_tree_map"].root.left.left.key, 8)
        self.assertEqual(
            self.tree_maps["only_right_tree_map"].root.left.left.parent.key, 7
        )

        # Values of nodes
        self.tree = TreeMap.parse_tuple((None, 1, None))
        for i in range(2, 15):
            self.tree.insert(i, i)
        self.assertEqual(self.tree.root.left.left.value, 4)
        self.assertEqual(self.tree.root.left.left.left.value, 8)
        self.assertEqual(self.tree.root.right.left.right.value, 13)

    def test_to_list(self):
        node1 = TreeNode(1, 1)
        node2 = TreeNode(2, 2)
        node3 = TreeNode(3, 3)
        # only root node in the tree
        self.tree_map = TreeMap(node1)
        self.assertEqual(self.tree_map.to_list(), [node1])

        # three nodes
        self.tree_map.insert_node(node2)
        self.tree_map.insert_node(node3)
        self.assertEqual(self.tree_map.to_list(), [node1, node2, node3])

        # different order of nodes
        self.tree_map = TreeMap(node3)
        self.tree_map.insert_node(node2)
        self.tree_map.insert_node(node1)
        self.assertEqual(self.tree_map.to_list(), [node1, node2, node3])

        # unbalanced tree
        self.assertEqual(
            self.tree_maps["tree_map"].to_list(),
            [
                TreeNode(1, None),
                TreeNode(2, None),
                TreeNode(5, None),
                TreeNode(6, None),
                TreeNode(7, None),
                TreeNode(9, None),
                TreeNode(9, None),
            ],
        )

    def test_insert_node(self):
        # adding node
        self.tree_maps["balanced_binary_tree_4_levels_height"].insert_node(
            TreeNode(1, 3)
        )
        self.tree_maps["balanced_binary_tree_4_levels_height"].insert_node(
            TreeNode(1, 3)
        )
        self.assertEqual(
            self.tree_maps[
                "balanced_binary_tree_4_levels_height"
            ].root.left.left.left.left.key,
            1,
        )
        self.assertEqual(
            self.tree_maps[
                "balanced_binary_tree_4_levels_height"
            ].root.left.left.left.right.key,
            1,
        )

        # adding to blank root
        self.tree_map = TreeMap(TreeNode(None, None))
        self.tree_map.insert_node(TreeNode(1, 2))
        self.assertEqual(self.tree_map.root.key, 1)
        self.assertIsNone(self.tree_map.root.left)

        # adding free node
        self.tree_map2 = TreeMap(TreeNode(1, None))
        node = TreeNode(3, None)
        self.tree_map2.insert_node(node)
        self.assertEqual(self.tree_map2.root.left, node)
        self.assertIs(self.tree_map2.root.left, node)

        # node already have parent
        self.tree_map.insert_node(TreeNode(1, None))
        self.tree_map3 = TreeMap(TreeNode(1, None))
        self.tree_map3.insert_node(self.tree_map.root.left)
        self.assertIsNotNone(self.tree_map.root.left.parent)
        self.assertEqual(self.tree_map3.root.left, self.tree_map.root.left)
        self.assertIsNot(self.tree_map3.root.left, self.tree_map.root.left)

        # node already have parent and childs
        self.tree_map4 = TreeMap(TreeNode(1, None))
        node = self.tree_maps["balanced_binary_tree_4_levels_height"].root.left
        self.assertIs(
            node, self.tree_maps["balanced_binary_tree_4_levels_height"].root.left
        )
        self.tree_map4.insert_node(node)
        self.assertEqual(node, self.tree_map4.root.left)
        self.assertIsNot(node, self.tree_map4.root.left)

    def test_eq_(self):
        node1 = TreeNode(1, 1)
        node2 = TreeNode(2, 2)
        node3 = TreeNode(3, 3)
        node4 = TreeNode(4, 4)
        node5 = TreeNode(4, 4)
        self.tree_map = TreeMap(node1)
        self.tree_map.insert_node(node2)
        self.tree_map.insert_node(node3)
        self.assertEqual(node1, node1)
        self.assertEqual(node5.left, node5.right)
        self.assertEqual(node5.left, None)
        # None None
        self.assertEqual(node5.left, node5.left)
        # node2 node2
        self.assertEqual(self.tree_map.root.left, self.tree_map.root.left)
        # node2 node3
        self.assertNotEqual(self.tree_map.root.right, self.tree_map.root.left)
        # node3 None
        self.assertNotEqual(self.tree_map.root.right, self.tree_map.root.right.right)
        self.assertEqual(self.tree_map.root.right.right, None)

        # same key values different parents and childs
        node1 = TreeNode(1, 1)
        node2 = TreeNode(2, 2)
        node3 = TreeNode(3, 3)
        node4 = TreeNode(2, 2)
        self.tree_map2 = TreeMap(node1)
        self.tree_map2.insert_node(node2)
        self.tree_map2.insert_node(node3)
        self.tree_map2.insert_node(node4)
        self.assertEqual(node2, node4)
        self.assertEqual(
            self.tree_map2.root.right.right, self.tree_map2.root.right.left
        )

    def test_is_child(self):
        pass

    def test_subtrees_eq(self):
        pass

    def test_find(self):
        self.assertEqual(self.tree_maps["tree_map"].find(5), [TreeNode(5, None)])

        # keys are repeating
        self.tree_maps["tree_map"].root.right.value = 5
        self.assertEqual(
            self.tree_maps["tree_map"].find(9), [TreeNode(9, 5), TreeNode(9, None)]
        )
        self.assertIs(
            self.tree_maps["tree_map"].find(5)[0],
            self.tree_maps["tree_map"].root.right.right.left,
        )
        self.tree_repeating = TreeMap(TreeNode(1, 1))
        self.tree_repeating.parse_list(
            [
                TreeNode(1, 1),
                TreeNode(2, 2),
                TreeNode(3, 3),
                TreeNode(5, 4),
                TreeNode(2, 5),
                TreeNode(2, 6),
                TreeNode(3, 7),
                TreeNode(3, 8),
                TreeNode(5, 9),
                TreeNode(5, 10),
                TreeNode(3, 11),
                TreeNode(4, 12),
                TreeNode(2, 13),
            ]
        )
        self.assertEqual(
            self.tree_repeating.find(5),
            [TreeNode(5, 9), TreeNode(5, 4), TreeNode(5, 10)],
        )
        self.assertEqual(
            self.tree_repeating.find(3),
            [TreeNode(3, 7), TreeNode(3, 3), TreeNode(3, 8), TreeNode(3, 11)],
        )
        self.assertEqual(
            self.tree_repeating.find(2),
            [TreeNode(2, 5), TreeNode(2, 2), TreeNode(2, 13), TreeNode(2, 6)],
        )
        # only root tree map
        self.tree = TreeMap(TreeNode(1, 1))
        self.assertEqual(self.tree.find(1), [TreeNode(1, 1)])

        # key not found
        self.assertEqual(self.tree_maps["tree_map"].find(15), None)

        # Wanted node at the end of the tree
        self.assertEqual(self.tree_maps["tree_map"].find(5)[0], TreeNode(5, None))
        self.assertIs(
            self.tree_maps["tree_map"].find(5)[0],
            self.tree_maps["tree_map"].root.right.right.left,
        )

    def test_update(self):
        pass

    ### TreeNode methods ###
    def test_is_free(self):
        free_node = TreeNode(1, 1)
        self.assertEqual(free_node.is_free(), True)

        bounded_node = TreeNode(1, 1)
        bounded_node2 = TreeNode(2, 2)
        bounded_node.insert(bounded_node2)
        self.assertEqual(bounded_node.is_free(), False)
        self.assertEqual(bounded_node2.is_free(), False)


if __name__ == "__main__":
    unittest.main()
