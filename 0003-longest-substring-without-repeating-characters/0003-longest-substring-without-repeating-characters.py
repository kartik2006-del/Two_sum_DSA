class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length=0
        left=0
        seen = set()
        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            max_length = max(max_length, right-left+1)
        return max_length

