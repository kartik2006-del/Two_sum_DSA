class Solution(object):
    def isAnagram(self, s, t):
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        freq1={}
        for j in t:
            if j in freq1:
                freq1[j]+=1
            else:
                freq1[j]=1
        return freq==freq1
                