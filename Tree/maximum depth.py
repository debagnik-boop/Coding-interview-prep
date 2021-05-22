# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        curr=root
        left=self.maxDepth(curr.left)
        right=self.maxDepth(curr.right)
        return max(left,right)+1
			
			
# Leet code link: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
