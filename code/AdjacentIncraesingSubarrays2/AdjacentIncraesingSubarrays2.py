class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        k = -math.inf

        #Sliding Window Problem

        l = 0

        lenArr = []

        for r in range(1,len(nums)):
            if nums[r-1] >= nums[r]:
                lenArr.append(r-l)
                l = r
        lenArr.append(r-l+1)
        
        for r in range(1,len(lenArr)):
            k = max(k,min(lenArr[r-1],lenArr[r]))
        
        if k >= max(lenArr)//2:
            return k
        else:
            return max(lenArr)//2