class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c**0.5)

        while l <= r:
            total = l * l + r * r
            if total == c:
                return True
            if total > c:
                r = r - 1
            else:
                l = l + 1

        return False