class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        total = 0 
        res = 0 

        for i in range(len(gas)): 
            total += gas[i]
            if total - cost[i] < 0 :
                total = 0
                res = i + 1
            else: 
                total -= cost[i]
        
        return res
