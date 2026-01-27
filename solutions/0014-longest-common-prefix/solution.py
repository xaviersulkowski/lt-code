class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest = min([len(x) for x in strs])
        for i in range(shortest):
            if len(set([s[i] for s in strs])) == 1:
                result += strs[0][i]
            else:
                break

        return result
