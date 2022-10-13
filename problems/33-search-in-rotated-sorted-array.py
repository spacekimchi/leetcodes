class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while i <= r:
            mid = l + (r - l) // 2
            mval, lval, rval = nums[mid], nums[l], nums[r]
            if mval == target:
                return mid
            elif target < mval:
                if mval < lval or target >= lval:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if mval > rval or target <= rval:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

