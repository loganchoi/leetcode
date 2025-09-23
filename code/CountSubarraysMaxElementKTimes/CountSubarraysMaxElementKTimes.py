class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        
        l = 0
        res = 0
        curK = 0
        for r in range(0,len(nums)):
            if nums[r] == maxVal:
                curK += 1
            while curK >= k:
                if nums[l] == maxVal:
                    curK -= 1
                l += 1
                res += (len(nums)-r)

        return res
            