# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        # Iterative
        if not root:
            return []
        stack, res = [], []
        while stack or root:
            if root:
                print("root val", root.val)
                stack.append(root)
                root = root.left
                print()
            else:
                node = stack.pop()
                print("node val", node.val)
                res.append(node.val)
                root = node.right
        return res
        '''
        # Recursive
        res = []
        self.helpler(root, res)
        return res
    
    def helpler(self, root, res):
        if root:
            self.helpler(root.left, res)
            res.append(root.val)
            self.helpler(root.right, res)
            
