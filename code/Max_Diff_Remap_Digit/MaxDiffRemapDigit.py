class Solution:
    def minMaxDifference(self, num: int) -> int:
        strNum = str(num)

        for i in range(0,len(strNum)):
            if strNum[i] != "9":
                break

        numChange = strNum[i]
        highNum = strNum.replace(numChange,"9")
        
        for i in range(0,len(strNum)):
            if strNum[i] != "0":
                break
        numChange = strNum[i]
        lowNum = strNum.replace(numChange,"0")

        print(highNum, lowNum)
        return int(highNum) - int(lowNum)