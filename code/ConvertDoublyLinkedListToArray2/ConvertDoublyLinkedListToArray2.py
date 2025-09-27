"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        #prepend
        res = []
        front = node
        while front.prev:
            front = front.prev
        
        back = front
        while back:
            res.append(back.val)
            back = back.next

        return res