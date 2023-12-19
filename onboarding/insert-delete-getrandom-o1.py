class RandomizedSet:

    def __init__(self):
        self.randomized= set()
        self.dic={}
        self.arr=[]

    def insert(self, val: int) -> bool:
        if val in self.randomized:
            return False
        self.randomized.add(val)
        self.dic[val]= len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.randomized:
            self.randomized.remove(val)
            self.arr[self.dic[val]]= 'Null'
            del self.dic[val]
            return True
        return False 
        

    def getRandom(self) -> int:
        random_number='Null'
        while random_number=='Null':
            random_number = random.choice(self.arr)
        return random_number
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()