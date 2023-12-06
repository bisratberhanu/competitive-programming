class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        prefixsum=[0]* (len(distance)+1)
        for i in range(1,len(distance)+1):
            prefixsum[i]= prefixsum[i-1]+ distance[i-1]
        print(prefixsum)
        candidate_1= abs(prefixsum[destination]-prefixsum[start])
        candidate_2= abs(sum(distance)-candidate_1)
        return min(candidate_1,candidate_2)
     
    

        