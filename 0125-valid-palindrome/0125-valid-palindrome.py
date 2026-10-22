class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        clean=''
        for i in s:
            if ('a'<=i<='z') or ('0'<=i<='9'):
                clean+=i
        return clean==clean[::-1]