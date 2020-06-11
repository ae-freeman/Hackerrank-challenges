# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
#
# Constraints:
#
# Both of the given trees will have between 1 and 200 nodes.
# Both of the given trees will have values between 0 and 200


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root_1_array = []
        root_2_array = []
        def leafSum1(root):


            if root is None:
                return
            if (root.left is None and root.right is None):
                root_1_array.append(root.val)


            leafSum1(root.left)
            leafSum1(root.right)

        def leafSum2(root):


            if root is None:
                return
            if (root.left is None and root.right is None):
                print("nothing either side")
                root_2_array.append(root.val)

                # total += root.val

            leafSum2(root.left)
            leafSum2(root.right)


        leafSum1(root1)
        leafSum2(root2)
        print(root_1_array)
        print(root_2_array)

        if root_1_array == root_2_array:
            return True
