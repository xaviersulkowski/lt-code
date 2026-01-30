class RandomizedSet:

    def __init__(self):
        self._set = {} # val to index in array map
        self._list = []

    def insert(self, val: int) -> bool:
        res = val not in self._set
        if res: 
            self._set[val] = len(self._list)
            self._list.append(val)
        return res 

    def remove(self, val: int) -> bool:
        res = val in self._set
        if res:
            # because we pop element from the list, we need to update indices in the set 
            # because we don't care about the order, we can replace poped value with latest element instead of moving the whole list
            idx = self._set[val]
            lastVal = self._list[-1]
            
            self._list[idx] = lastVal
            self._list.pop(-1)
            self._set[lastVal] = idx
            self._set.pop(val)
            
        return res
        
    def getRandom(self) -> int:
        return random.choice(self._list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
