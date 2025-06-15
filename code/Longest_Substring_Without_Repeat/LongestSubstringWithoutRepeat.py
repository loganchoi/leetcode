class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Start with two pointers at the beginning of the array
        l = r = 0
        #Also have a SET of values that are currently within the window
        charSet = set()

        maxString = 0

        #As the right pointer moves along, keep adding it to the charSet
        #If a character is already within the set, move the left pointer until it is popped

        for r in range(0,len(s)):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l = l + 1
            charSet.add(s[r])
            maxString = max(maxString,(r-l+1))

        return maxString