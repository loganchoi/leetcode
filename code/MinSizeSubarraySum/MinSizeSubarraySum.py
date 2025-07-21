class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = math.inf

        l = 0 
        total = 0
        for r in range(0,len(nums)):
            total = total + nums[r]
            while total >= target:
                total = total - nums[l]
                minLen = min(minLen,r-l+1)
                l = l + 1

        if minLen == math.inf:
            return 0
        return minLen