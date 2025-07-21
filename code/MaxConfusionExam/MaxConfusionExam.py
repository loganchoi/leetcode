class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0 
        maxLen = 0
        convert = 0

        #Check for consecutive Trues
        for r in range(0,len(answerKey)):
            if answerKey[r] == "F":
                convert = convert + 1
            while convert > k:
                if answerKey[l] == "F":
                    convert = convert - 1
                l = l + 1
            
            maxLen = max(maxLen,r-l+1)
        
        l = 0
        convert = 0
        #Check for consecutive Falses
        for r in range(0,len(answerKey)):
            if answerKey[r] == "T":
                convert = convert + 1
            while convert > k:
                if answerKey[l] == "T":
                    convert = convert - 1
                l = l + 1
            
            maxLen = max(maxLen,r-l+1)
        

        return maxLen