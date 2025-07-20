class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        v = ['a','e','i','o','u']
        vSet = set(v)

        for char in s:
            if char.lower() in vSet:
                vowels.append(char)
        
        vowels.sort()
        print(vowels)
        ans = ""

        for char in s:
            if char.lower() in vSet:
                ans = ans + vowels.pop(0)
            else:
                ans = ans + char
        
        return ans