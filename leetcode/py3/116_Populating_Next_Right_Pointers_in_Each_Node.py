"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from queue import Queue

class Solution:
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        return self.level_traverse(root)


    def level_traverse(self, root):
        """
        层序遍历的方式
        """
        if not root:
            return root
        
        q = Queue()
        q.put(root)
        
        while not q.empty():
            # 第一层从上到下便利
            i = 0
            sz = q.qsize()
            last_node = None
            while i < sz:
                # 第二层从左到右
                cur = q.get()
                
                left =  cur.left
                right = cur.right
                    
                if left and right:
                    
                    if last_node:
                        last_node.next = left
                    
                    left.next = right
                    last_node = right
                    
                    q.put(left)
                    q.put(right)
                i += 1
        
        return root
