# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        self.traverse(root)
    
    def traverse(self, root):
        
        if root == None:
            return
        
        self.traverse(root.left)
        self.traverse(root.right)
    
        left = root.left
        right = root.right
        
        root.left = None
        root.right = left
        
        p = root
        while p.right != None:
            p = p.right
        
        p.right = right
