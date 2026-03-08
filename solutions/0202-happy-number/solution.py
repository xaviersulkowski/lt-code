class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n

        while number not in seen: 
            seen.add(number)
            number = self.square(number)
            if number == 1: 
                return True
        
        return False
    
    def square(self, n: int): 
        output = 0 

        while n: 
            digit = n % 10 
            digit = digit ** 2 
            output += digit 
            n = n // 10

        return output
