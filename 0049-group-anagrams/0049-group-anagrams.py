class Solution(object):
    def groupAnagrams(self, strs):
        groups={}
        for words in strs:
            key=''.join(sorted(words))
            if key not in groups:
                groups[key]=[]
            groups[key].append(words)
        return list(groups.values())
        