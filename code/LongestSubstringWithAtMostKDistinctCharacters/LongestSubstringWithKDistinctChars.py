class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0

        res = 0
        charCount = defaultdict(int)
        for r in range(0,len(s)):
            charCount[s[r]] = charCount[s[r]] + 1
            while len(charCount) > k:
                charCount[s[l]] -= 1
                if charCount[s[l]] == 0:
                    del charCount[s[l]]
                l += 1
            res = max(r-l+1,res)

        return res    