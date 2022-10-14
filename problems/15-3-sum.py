class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        m = set()
        n = len(nums)
        checked = set()
        for i, num in enumerate(nums):
            s = set()
            j = i+1
            while j < n and num not in checked:
                val = nums[j]
                target = (val + num) * -1
                sor = sorted([str(num), str(val), str(target)])
                st = ",".join(sor)
                if target in s and st not in m:
                    ans.append([num, val, target])
                    m.add(st)
                j += 1
                s.add(val)
            checked.add(num)
        return ans
