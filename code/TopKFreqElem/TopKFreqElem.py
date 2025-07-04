class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = collections.Counter(nums)
        heap = []
        for x in numsDict.keys():
            heapq.heappush(heap,(-numsDict[x],x))

        res = []

        for x in range(0,k):
            num = heapq.heappop(heap)[1]
            res.append(num)

        return res