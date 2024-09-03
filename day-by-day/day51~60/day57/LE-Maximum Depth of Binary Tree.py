
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root:
            return 0
        
        dq = deque([root])
        step = 0
        while dq:
            len_node = len(dq)
            for i in range(len_node):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                elif node.right:
                    dq.append(node.right)
            step += 1
        
        return step