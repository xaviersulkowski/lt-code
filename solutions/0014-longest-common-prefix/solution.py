class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = "" 
        min_len = min([len(s) for s in strs])
        for i in range(min_len): 
            if len(set([s[i] for s in strs])) == 1: 
                result += strs[0][i]
            else: 
                break

        return result
