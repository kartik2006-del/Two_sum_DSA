# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def validate(node,low,high):
            if not node:
                return True
            if node.val>=high or node.val<=low:
                return False
            left=validate(node.left,low,node.val)
            right=validate(node.right,node.val,high)
            return left and right
        return validate(root,float('-inf'),float('inf'))