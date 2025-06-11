class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        res = []
        length = len(nums)
        for num in count.keys():
            if count[num] > length/3:
                res.append(num)

        return res