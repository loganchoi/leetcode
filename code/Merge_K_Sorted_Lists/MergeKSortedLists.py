# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        import heapq as hq

        curNode = ListNode()
        ans = curNode
        vals = []
        for l in lists:
            node = l
            print(node)
            while node != None:
                hq.heappush(vals,node.val)
                node = node.next

        while vals != []:
            v = hq.heappop(vals)
            newNode = ListNode(v)
            curNode.next = newNode
            curNode = curNode.next

        return ans.next 