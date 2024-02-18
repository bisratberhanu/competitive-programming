class RecentCounter:

    def __init__(self):
       self.queue= []  

    def ping(self, t: int) -> int:
        self.queue.append(t)
        rangee= t-3000
        counter=0
        i= len(self.queue)-1
        while i>=0 and self.queue[i]>= rangee:
            counter+=1
            i-=1
        return counter 

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)