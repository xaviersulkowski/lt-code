class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        sieve = self._sieve(right)
        prime_numbers = [x for x in range(left, right + 1) if sieve[x]]

        min_pair = [-1, -1]
        min_length = float('inf')
        
        last_pair = []
        
        for x in prime_numbers: 
            last_pair.append(x)
            if len(last_pair) == 2: 
                if ((last_pair[1] - last_pair[0]) < min_length):
                    min_pair = [last_pair[0], last_pair[1]]
                    min_length = last_pair[1] - last_pair[0]
                last_pair = []
                last_pair.append(x)

        return min_pair


    def _sieve(self, upper_limit):
        # Create an integer list to mark prime numbers (True = prime, False = not prime)
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for number in range(2, int(upper_limit**0.5) + 1):
            if sieve[number]:
                # Mark all multiples of 'number' as non-prime
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        return sieve
