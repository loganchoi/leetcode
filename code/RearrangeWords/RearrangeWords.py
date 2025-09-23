class Solution:
    def arrangeWords(self, text: str) -> str:
        lenMap = {}

        words = text.split(" ")

        for w in words:
            wordLen = len(w)
            if wordLen in lenMap.keys():
                lenMap[wordLen].append(w.lower())
            else:
                lenMap[wordLen] = [w.lower()]
        
        nums = sorted(lenMap.keys())

        res = ""
        for n in nums:
            for w in lenMap[n]:
                res += " " + w

        return res.strip().capitalize()