class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = 0
        r = 9

        if len(s) < 10:
            return []

        res = []

        genomes = set()
        alreadyAdded = set()

        while r < len(s):
            if s[l:r+1] not in genomes:
                genomes.add(s[l:r+1])
            elif s[l:r+1] not in alreadyAdded:
                alreadyAdded.add(s[l:r+1])
                res.append(s[l:r+1])
            l += 1
            r += 1

        return res