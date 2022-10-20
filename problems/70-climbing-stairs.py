class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        a, b = 2, 1
        for i in range(2, n):
            a, b = a+b, a
        return a

