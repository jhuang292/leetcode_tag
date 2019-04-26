# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        '''
        res = []
        self.helpler(root, res)
        return res
    
    def helpler(self, root, res):
        if root:
            self.helpler(root.left, res)
            self.helpler(root.right, res)
            res.append(root.val)
           '''
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
        
