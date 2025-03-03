class Solution:
    def reverse(self, x: int) -> int:

        if (-10 < x < 10):
            return x
        
        int_32_range_low = "2147483648"
        int_32_range_high = "2147483647"

        is_minus, x = x < 0, abs(x)

        range_to_compare = int_32_range_low if is_minus else int_32_range_high
        
        if (len(str(x)) > len(range_to_compare)):
            return 0
        
        max_len = len(str(x))

        possible_overflow = len(str(x)) == len(range_to_compare)

        res = 0
        i = 0 

        while i < max_len:
            modulo = x % 10 

            if i > 0:
                res *= 10
            res += modulo 
            x = x // 10  

            i += 1 

            if possible_overflow and res > int(range_to_compare[:i]):
                return 0
                    
        if (is_minus):
            return -res 
        else: 
            return res 
