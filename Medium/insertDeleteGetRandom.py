class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        res = val in self.numMap
        if not res:
            self.numMap[val] = len(self.arr)
            self.arr.append(val)
        return not res
        
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        
        if res:
            index = self.numMap[val]
            lastVal = self.arr[-1]
            self.arr[index] = lastVal
            self.numMap[lastVal] = index
            self.numMap.pop(val)
            self.arr.pop()
            
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()