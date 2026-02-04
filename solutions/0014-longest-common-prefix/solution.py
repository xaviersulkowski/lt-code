class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # approach 1 
        # result = "" 
        # min_len = min([len(x) for x in strs])
        # for i in range(min_len): 
        #     if len(set([strs[j][i] for j in range(len(strs))])) == 1: 
        #         result += strs[0][i] 
        #     else: 
        #         break
        # return result
        # approach 2 
        result = ""
        strs.sort()
        min_len = min([len(x) for x in strs])

        for i in range(min_len): 
            if strs[0][i] == strs[-1][i]: 
                result += strs[0][i]
            else: 
                break
        return result

                

