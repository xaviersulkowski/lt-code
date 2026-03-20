class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): 
            return -1 

        tank = 0 
        pos = 0 
        for i in range(len(gas)): 
            tank += gas[i]
            if tank - cost[i] < 0: 
                tank = 0 
                pos = i + 1 
            else: 
                tank -= cost[i]

        return pos
            

    
