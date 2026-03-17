class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # approach 1 with seen hashmap 
        # seen = {}
        # for i in range(len(numbers)): 
        #     diff = target - numbers[i]
        #     if diff in seen: 
        #         return [seen[diff] + 1, i + 1]
        #     seen[numbers[i]] = i
        # return False
    
        # approach 2 two pointers 
        l = 0
        r = len(numbers) - 1 

        while l < r: 
            sum_ = numbers[l] + numbers[r]
            if sum_ > target: 
                r -= 1 
            if sum_ < target: 
                l += 1 
            if sum_ == target: 
                return [l+1,r+1]

