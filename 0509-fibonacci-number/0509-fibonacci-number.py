class Solution(object):
    def fib(self, n):
        memo={}
        def me(n):
            if n==1 :
                return 1
            elif n==0:
                return 0
            if n in memo:
                return memo[n]
            memo[n]=me(n-1)+me(n-2)
            return memo[n]
        return me(n)

        