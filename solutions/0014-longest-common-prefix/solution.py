class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        shortest = strs[0]
        
        prefix = ""
        
        for s in shortest:
            
            prefix_candidate = prefix + s
            
            if not all([s.startswith(prefix_candidate) for s in strs]):
                break 
            else: 
                prefix = prefix_candidate 
        
        return prefix
