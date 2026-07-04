# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, mn, mx):
        if root is None:
            return True
        if root.val<mn or root.val>mx:
            return False
        checkLeft = self.check(root.left,mn,root.val-1)
        checkRight = self.check(root.right, root.val+1, mx)
        return checkLeft and checkRight

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -1000000000000, 1000000000000)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna