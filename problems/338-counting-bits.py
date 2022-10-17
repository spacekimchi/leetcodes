class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        ceil, cur = 1, 0
        ans = [0,1]
        for i in range(2,n+1):
            cur += 1
            if ceil == cur:
                ceil *= 2
                cur = 0
            ans.append(1 + ans[cur])
        return ans

