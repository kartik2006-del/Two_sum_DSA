class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq={}
        for i in magazine:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for j in ransomNote:
            if j not in freq or freq[j]==0:
                return False
            freq[j]-=1
        return True