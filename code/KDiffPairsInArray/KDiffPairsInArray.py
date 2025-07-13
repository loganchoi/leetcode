class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        lptr = rptr = 0
        seen = set()

        while rptr < len(nums):
            if (nums[rptr] - nums[lptr] == k 
                and (nums[lptr],nums[rptr]) not in seen
                and rptr != lptr):
                seen.add((nums[lptr],nums[rptr]))
                rptr = rptr + 1
                lptr = lptr + 1
            elif nums[rptr] - nums[lptr] > k:
                lptr = lptr + 1
            else:
                rptr = rptr + 1

        return len(seen)
