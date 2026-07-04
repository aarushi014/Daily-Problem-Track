# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        if abs(left_h - right_h) > 1:
            self.ans = False
        return max(left_h, right_h) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna