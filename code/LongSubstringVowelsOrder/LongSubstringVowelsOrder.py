class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        l = 0  
        r = 0
        for r in range(1,len(word)):
            if ord(word[r]) < ord(word[r-1]):
                if len(set(word[l:r])) == 5:
                    res = max(res,r-l)
                l = r
    
        if len(set(word[l:])) == 5:
            res = max(res,r-l+1)

        return res