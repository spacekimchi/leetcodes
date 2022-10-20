class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            if len(stk) == 0 or stk[-1] < num:
                stk.append(num)
            else:
                idx = bisect_left(stk, num)
                stk[idx] = num
        return len(stk)

