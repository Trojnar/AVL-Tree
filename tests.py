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

    # def _display_test_cases(self):
    #     # Helper method for debugging
    #     for tree_map in self.tree_maps:
    #         tree_map.display_keys()

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
        self.assertEqual(
            self.tree_maps["balanced_binary_tree_4_levels_height"].traverse_inorder(),
            [4, 10, 12, 15, 18, 22, 24, 25, 31, 25, 44, 50, 66, 70, 90],
        )
        self.assertEqual(
            self.tree_maps["balanced_binary_tree_3_levels_height"].traverse_inorder(),
            [4, 2, 5, 1, 6, 3, 7],
        )

    def test_traverse_preorder(self):
        self.assertEqual(
            self.tree_maps["balanced_binary_tree_4_levels_height"].traverse_preorder(),
            [25, 15, 10, 4, 12, 22, 18, 24, 50, 25, 31, 44, 70, 66, 90],
        )
        self.assertEqual(
            self.tree_maps["balanced_binary_tree_3_levels_height"].traverse_preorder(),
            [1, 2, 4, 5, 3, 6, 7],
        )

    def test_traverse_postorder(self):
        self.assertEqual(
            self.tree_maps["balanced_binary_tree_4_levels_height"].traverse_postorder(),
            [4, 12, 10, 18, 24, 22, 15, 31, 44, 25, 66, 90, 70, 50, 25],
        )
        self.assertEqual(
            self.tree_maps["balanced_binary_tree_3_levels_height"].traverse_postorder(),
            [4, 5, 2, 6, 7, 3, 1],
        )

    def test_insert_method(self):
        # blank on the left at 3rd level in 5 level tree
        self.tree_maps["tree_map"].insert(1, None)
        self.assertEqual(self.tree_maps["tree_map"].root.right.left.key, 1)
        self.assertEqual(self.tree_maps["tree_map"].root.right.left.parent.key, 9)
        self.tree_maps["tree_map"].insert(3, None)
        self.tree_maps["tree_map"].root.display_keys()
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



if __name__ == "__main__":
    unittest.main()
