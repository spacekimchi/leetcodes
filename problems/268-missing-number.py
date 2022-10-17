class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            ans ^= i+1
            ans ^= nums[i]
        return ans

