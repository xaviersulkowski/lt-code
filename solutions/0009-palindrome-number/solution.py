class Solution:
    def isPalindrome(self, x: int) -> bool:        
        x_str = str(x)
        i = 0 

        while i < (len(x_str) // 2): 
            if(x_str[i] == x_str[-1 - i]):
                i += 1
                continue 
            else: 
                return False
        return True
