class UndergroundSystem:

    def __init__(self):
        self.check_in= defaultdict(list)
        self.avg_time= defaultdict(int)
        self.count= defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id]= [stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.avg_time[str(self.check_in[id][0])+'-'+stationName]+=t-self.check_in[id][1]
        self.count[str(self.check_in[id][0])+'-'+stationName]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_time[startStation+'-'+endStation]/ self.count[startStation+'-'+endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)