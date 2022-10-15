class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        print(n)
        l, r = 0, n - 1
        ans = 0
        while l < r:
            lh, rh = height[l], height[r]
            area = min(lh, rh) * (r - l)
            ans = max(ans, area)
            if lh < rh:
                l += 1
            else:
                r -= 1
        return ans

