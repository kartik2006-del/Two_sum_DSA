class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs = {')':'(', ']':'[', '}':'{'}
        for i in range(len(s)):
            char=s[i]
            if char=='(' or char=='[' or char=='{':
                stack.append(char)
            elif char==')' or char==']' or char=='}':
                if not  stack :
                    return False
                if stack[-1]==pairs[char]:
                    stack.pop()
                else :
                    return False
        return len(stack)==0



        
        