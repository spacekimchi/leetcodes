class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        cur_min, cur_max = nums[0], nums[0]
        for i in range(1, n):
            num = nums[i]
            if num == 0:
                cur_max, cur_min = 0, 0
            else:
                cur_min, cur_max = min(cur_min * num, cur_max * num, num), max(cur_min * num, cur_max * num, num)
            ans = max(ans, cur_max, cur_min)
        return ans

