class Solution(object):
    def climbStairs(self, n):
        memo={}
        def slove(n):
            if n==0 or n==1:
                return 1
            if n in memo:
                return memo[n]
            memo[n]=slove(n-1)+slove(n-2)
            return memo[n]
        return slove(n)         