# type: ignore

from unittest import TestCase
import unittest
from tree import TreeMap, TreeNode
from bst import BSTMap, BSTNode
from rbt import RBTMap, RBTNode


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
        self.assertEqual(self.tree_maps["tree_map"].height(), 3)
        self.assertEqual(self.tree_maps["only_right_tree_map"].height(), 3)
        self.assertEqual(self.tree_maps["only_left_tree_map"].height(), 3)

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

        # node already have parent and children
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

        # same key values different parents and children
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

    def test_find_by_node(self):
        self.assertEqual(
            self.tree_maps["tree_map"].find_node(TreeNode(5, None)), TreeNode(5, None)
        )
        self.assertEqual(
            self.tree_maps["tree_map"].find_node(TreeNode(9, None)), TreeNode(9, None)
        )

        # find blank node
        self.assertEqual(
            self.tree_maps["tree_map"].find_node(TreeNode(None, None)), None
        )

        # Node not found
        self.assertEqual(self.tree_maps["tree_map"].find_node(TreeNode(3, None)), None)

        # only root tree map
        self.tree = TreeMap(TreeNode(1, 1))
        self.assertEqual(self.tree.find_node(TreeNode(1, 1)), TreeNode(1, 1))

        # Wanted node at the end of the tree
        self.assertEqual(self.tree_maps["tree_map"].find(5)[0], TreeNode(5, None))
        self.assertIs(
            self.tree_maps["tree_map"].find_node(TreeNode(5, None)),
            self.tree_maps["tree_map"].root.right.right.left,
        )

        # Nodes repeats/ keys repeats
        self.tree_repeating = TreeMap(TreeNode(1, 1))
        self.tree_repeating.parse_list(
            [
                TreeNode(1, 1),
                TreeNode(2, None),
                TreeNode(3, 3),
                TreeNode(5, 4),
                TreeNode(2, 2),
                TreeNode(2, 6),
                TreeNode(3, 8),
                TreeNode(3, 8),
                TreeNode(5, 9),
                TreeNode(5, None),
                TreeNode(3, 11),
                TreeNode(4, 12),
                TreeNode(2, 13),
            ]
        )
        node = self.tree_repeating.find_node(TreeNode(5, 9))
        self.assertIs(node, self.tree_repeating.root.left.right.left)
        self.assertEqual(node, TreeNode(5, 9))

        node = self.tree_repeating.find_node(TreeNode(3, 3))
        self.assertEqual(
            self.tree_repeating.find_node(TreeNode(3, 3)),
            TreeNode(3, 3),
        )
        self.assertIs(node, self.tree_repeating.root.left.left)

        # repeating value
        node = self.tree_repeating.find_node(TreeNode(3, 8))
        self.assertEqual(
            node,
            TreeNode(3, 8),
        )
        self.assertIs(node, self.tree_repeating.root.left.left.left)

        node = self.tree_repeating.find_node(TreeNode(5, None))
        self.assertEqual(
            node,
            TreeNode(5, None),
        )
        self.assertIs(node, self.tree_repeating.root.left.right.right)

        self.assertEqual(
            self.tree_maps["tree_map"].find_node(TreeNode(1, None)), TreeNode(1, None)
        )

    def test_update(self):
        self.tree_maps["tree_map"].update(TreeNode(9, None), 5)
        self.assertEqual(self.tree_maps["tree_map"].root.right.value, 5)

        self.tree_maps["tree_map"].update(TreeNode(1, None), 5)
        self.assertEqual(self.tree_maps["tree_map"].root.value, 5)

    def test_subtrees_eq_and_magic_eq(self):
        tree_map = TreeMap(TreeNode(1, 1))
        tree_map2 = TreeMap(TreeNode(1, 1))
        result = tree_map.subtrees_eq(tree_map.root, tree_map2.root)
        self.assertTrue(result)
        self.assertTrue(tree_map == tree_map2)
        tree_map.insert(3, 8)
        tree_map2.insert(3, 8)
        result = tree_map.subtrees_eq(tree_map.root, tree_map2.root)
        self.assertTrue(result)
        self.assertTrue(tree_map == tree_map2)
        tree_map.insert(5, 10)
        tree_map2.insert(3, 2)
        result = tree_map.subtrees_eq(tree_map.root, tree_map2.root)
        self.assertFalse(result)
        self.assertFalse(tree_map == tree_map2)

    def test_is_parent_of(self):
        node1 = self.tree_maps["tree_map"].root
        node2 = self.tree_maps["tree_map"].root.left.left
        self.assertTrue(node1.is_parent_of(node2))
        self.assertFalse(node1.is_parent_of(TreeNode(1, None)))
        self.assertFalse(node1.is_parent_of(None))

    def test_is_child_of(self):
        node1 = self.tree_maps["tree_map"].root
        node2 = self.tree_maps["tree_map"].root.left.left
        self.assertTrue(node2.is_child_of(node1))
        self.assertFalse(node1.is_child_of(TreeNode(1, None)))
        self.assertFalse(node2.is_child_of(TreeNode(1, None)))
        self.assertFalse(node1.is_child_of(None))

    def test_is_full(self):
        self.assertTrue(
            self.tree_maps["tree_map"].is_full(self.tree_maps["tree_map"].root, 0)
        )
        self.assertTrue(
            self.tree_maps["tree_map"].is_full(self.tree_maps["tree_map"].root, 1)
        )
        self.assertFalse(
            self.tree_maps["tree_map"].is_full(self.tree_maps["tree_map"].root, 3)
        )
        self.assertFalse(
            self.tree_maps["tree_map"].is_full(self.tree_maps["tree_map"].root, 4)
        )

    def test_is_max_left(self):
        self.assertTrue(self.tree_maps["tree_map_last_blank"].is_max_left())
        self.assertFalse(self.tree_maps["tree_map"].is_max_left())

    def test_is_complete(self):
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

    def test_find_rightmost(self):
        self.assertEqual(
            self.tree_maps["tree_map"]
            .root._find_rightmost(self.tree_maps["tree_map"].height())
            .key,
            5,
        )

    def test_remove(self):
        self.assertEqual(
            self.tree_maps["tree_map"].root.right.right.left, TreeNode(5, None)
        )
        self.assertEqual(self.tree_maps["tree_map"].root.left, TreeNode(7, None))
        self.tree_maps["tree_map"].remove(TreeNode(7, None))
        self.assertEqual(
            self.tree_maps["tree_map"].root.right.right.left, TreeNode(None, None)
        )
        self.assertEqual(self.tree_maps["tree_map"].root.left, TreeNode(5, None))

        # delete root
        self.assertEqual(self.tree_maps["tree_map"].root.right.right, TreeNode(9, None))
        self.assertEqual(self.tree_maps["tree_map"].root, TreeNode(1, None))
        self.tree_maps["tree_map"].remove(TreeNode(1, None))
        self.assertEqual(self.tree_maps["tree_map"].root, TreeNode(9, None))
        self.assertEqual(
            self.tree_maps["tree_map"].root.right.right, TreeNode(None, None)
        )

        # delete rightmost
        self.assertEqual(self.tree_maps["tree_map"].root.left.right, TreeNode(6, None))
        self.tree_maps["tree_map"].remove(TreeNode(6, None))
        self.assertEqual(
            self.tree_maps["tree_map"].root.left.right, TreeNode(None, None)
        )

    def test_inorder_successor(self):
        tree = self.tree_maps["tree_map"]
        tree.display_keys()
        self.assertEqual(tree.root.inorder_successor().key, 9)
        self.assertEqual(tree.root.left.inorder_successor().key, 6)
        self.assertEqual(tree.root.right.inorder_successor().key, 5)

    def test_inorder_predecessor(self):
        tree = self.tree_maps["tree_map"]
        tree.display_keys()
        self.assertEqual(tree.root.inorder_predecessor().key, 6)
        self.assertEqual(tree.root.left.inorder_predecessor().key, 2)
        self.assertEqual(tree.root.right.inorder_predecessor().key, 1)


class BSTTest(TestCase):
    def setUp(self):
        self.test_cases = [
            # 0
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
            # 1
            (
                ((None, 4, None), 2, (None, 5, None)),
                1,
                ((None, 6, None), 3, (None, 7, None)),
            ),
            # 2
            (
                ((None, 2, None), 7, (None, 6, None)),
                1,
                (None, 9, ((None, 5, None), 9, None)),
            ),
        ]
        self._set_treemaps()

    def _set_treemaps(self):
        self.tree_maps = {
            "first_tree": BSTMap.parse_tuple(self.test_cases[0]),
        }

    def test_insert(self):
        self.tree_maps["first_tree"].insert(5, None)
        self.assertEqual(self.tree_maps["first_tree"].root.left.left.left.right.key, 5)
        self.tree_maps["first_tree"].insert(3, None)
        self.assertEqual(self.tree_maps["first_tree"].root.left.left.left.left.key, 3)
        self.tree_maps["first_tree"].insert(120, None)
        self.assertEqual(
            self.tree_maps["first_tree"].root.right.right.right.right.key, 120
        )
        len_bef = self.tree_maps["first_tree"].length()
        self.tree_maps["first_tree"].insert(15, None)
        self.assertEqual(len_bef, self.tree_maps["first_tree"].length())

        # reuturns insterted node
        node = self.tree_maps["first_tree"].insert(89, None)
        print(repr(node))

    def test_find(self):
        node = self.tree_maps["first_tree"].find(15)
        self.assertIsInstance(node, BSTNode)
        self.assertIs(self.tree_maps["first_tree"].root.left, node)

    def test_is_bst(self):
        self.assertTrue(self.tree_maps["first_tree"].is_bst())

    def test_parse_tuple(self):
        not_bst = self.test_cases[1]
        not_balanced_bst_with_duplicate = self.test_cases[2]
        with self.assertRaises(ValueError):
            BSTMap.parse_tuple(not_bst),
        with self.assertRaises(ValueError):
            BSTMap.parse_tuple(not_balanced_bst_with_duplicate),
        self.assertNotEqual(self.tree_maps["first_tree"], False)
        self.assertIsInstance(self.tree_maps["first_tree"], BSTMap)

    def test_parse_list(self):
        l = [
            BSTNode(5, None),
            BSTNode(8, None),
            BSTNode(10, None),
            BSTNode(11, None),
            BSTNode(12, "Some Value"),
            BSTNode(4, None),
            BSTNode(14, None),
        ]
        tree = BSTMap.parse_list(l)
        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.root.left.key, 4)
        self.assertEqual(tree.root.right.key, 8)
        self.assertEqual(tree.root.right.right.key, 10)
        self.assertEqual(tree.root.right.right.right.key, 11)
        self.assertEqual(tree.root.right.right.right.right.key, 12)
        self.assertEqual(tree.root.right.right.right.right.right.key, 14)

        l2 = [
            (5, None),
            (8, None),
            (10, None),
            (11, None),
            (12, "Some Value"),
            (4, None),
            (14, None),
        ]
        tree2 = BSTMap.parse_list(l2)

        l3 = [
            [5, None],
            [8, None],
            [10, None],
            [11, None],
            [12, "Some Value"],
            [4, None],
            [14, None],
        ]
        tree3 = BSTMap.parse_list(l3)

        # Every tree is the same
        self.assertEqual(tree, tree2)
        self.assertTrue(tree2, tree3)

    def test_remove(self):
        tree = self.tree_maps["first_tree"]

        # remove leaf
        self.assertEqual(tree.root.left.left.left, BSTNode(4, None))
        self.tree_maps["first_tree"].remove(4)
        self.assertEqual(tree.root.left.left.left, BSTNode(None, None))

        # remove node with one child
        self.assertEqual(tree.root.left.left, BSTNode(10, None))
        self.tree_maps["first_tree"].remove(10)
        self.assertEqual(tree.root.left.left, BSTNode(12, None))
        self.assertEqual(tree.root.left.left.right, BSTNode(None, None))

        # remove node with two children
        self.assertEqual(tree.root.left, BSTNode(15, None))
        self.assertEqual(tree.root.left.right.left, BSTNode(18, None))
        self.tree_maps["first_tree"].remove(15)
        self.assertEqual(tree.root.left, BSTNode(18, None))
        self.assertEqual(tree.root.left.right.left, BSTNode(None, None))

        # remove root
        self.assertEqual(tree.root, BSTNode(25, None))
        self.assertEqual(tree.root.right.left.left, BSTNode(31, None))
        self.tree_maps["first_tree"].remove(25)
        self.assertEqual(tree.root, BSTNode(31, None))
        self.assertEqual(tree.root.right.left.left, BSTNode(None, None))


class RBTTest(TestCase):
    def test_setter(self):
        node = RBTNode(1, None)
        self.assertIsInstance(node.left, RBTNode)
        self.assertIsInstance(node.right, RBTNode)
        self.assertEqual(node.right, RBTNode(None, None))
        self.assertEqual(node.left, RBTNode(None, None))
        self.assertEqual(node.right.right, None)
        self.assertEqual(node.right.left, None)
        self.assertEqual(node.left.left, None)
        self.assertEqual(node.left.right, None)
        self.assertEqual(node.left.color, "black")
        self.assertEqual(node.right.color, "black")


if __name__ == "__main__":
    unittest.main()
