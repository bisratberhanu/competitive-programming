class OrderedStream:

    def __init__(self, n: int):
        self.ptr=1
        self.ans=[]
        self.dic={}
    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey]= value
        temp= self.ptr
        while True:
            if self.ptr not in self.dic:
                break
            self.ptr+=1
        temp_list=[]
        for i in range(temp,self.ptr):
            temp_list.append(self.dic[i])
            
        return temp_list


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)