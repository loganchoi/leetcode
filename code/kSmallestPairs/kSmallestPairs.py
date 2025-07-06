class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []

        for x in nums1:
            for y in nums2:
                total = x+y
                if len(heap) == k:
                    if heap[0][0] < -total:
                        heapq.heappop(heap)
                        heapq.heappush(heap,(-total, [x,y]))
                    else:
                        break
                else:
                    heapq.heappush(heap,(-total,[x,y]))

        res = []

        for _, vals in heap:
            res.append(vals)

        return res