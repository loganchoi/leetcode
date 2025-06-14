class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(curArr):
            if len(curArr) == len(nums):
                ans.append(curArr[:])
                return
            else:
                for x in range(0,len(nums)):
                    if nums[x] not in curArr:
                        curArr.append(nums[x])
                        helper(curArr)
                        curArr.pop()


        helper([])
        return ans
        