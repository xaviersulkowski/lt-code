class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_normalized = "".join([s for s in s.lower() if s.isalnum()])
        

        if len(s_normalized) <= 1: 
            return True 
        
        for i in range(0, len(s_normalized)//2): 
            if s_normalized[i] != s_normalized[-1 - i]:
                return False
        
        return True 
        
