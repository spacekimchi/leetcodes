class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        postfix_sum = [0] * (n + 1)
        s = 0
        for i, num in reversed(list(enumerate(nums))):
            postfix_sum[i] = postfix_sum[i + 1] + num
            # [28, 27, 20, 17, 11,  6, 0]
        for i in range(n):
            if s == postfix_sum[i + 1]:
                return i
            s += nums[i]
        return -1
