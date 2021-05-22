# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals targetSum.

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        if (target==root.val and root.left==None and root.right==None):
            return True
        leftAns=self.hasPathSum(root.left,target-root.val)
        rightAns=self.hasPathSum(root.right,target-root.val)
        return leftAns or rightAns
			
# Leet code problem link: https://leetcode.com/problems/path-sum/
