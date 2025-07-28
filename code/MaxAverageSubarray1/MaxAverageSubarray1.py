class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        nextTotal = total
        l = 0
        for r in range(k,len(nums)):
            nextTotal = nextTotal - nums[l] + nums[r]
            l = l+1
            total = max(total,nextTotal)

        return total/k