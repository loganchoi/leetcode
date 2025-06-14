class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(currArr,index):
            if len(nums) == len(currArr):
                ans.append(currArr[:])
                return
            else:
                ans.append(currArr[:])
                for x in range(index,len(nums)):
                    currArr.append(nums[x])
                    backtrack(currArr,x+1)
                    currArr.pop()

        backtrack([],0)

        return ans