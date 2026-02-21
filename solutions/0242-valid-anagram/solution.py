class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        ss = {} 

        for i in s: 
            i = ord(i)
            ss[i] = ss.get(i, 0) + 1
        
        for i in t: 
            i = ord(i)
            if i not in ss: 
                return False 
            else:
                ss[i] -= 1 
                if ss[i] == 0: 
                    del ss[i]
        
        if len(ss) > 0: 
            return False

        return True 


