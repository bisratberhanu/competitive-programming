class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        prefix=0
        counter=0
        for i in range(len(flips)):
            n= i+1
            prefix+=flips[i]
            if prefix== n*(n+1)/2:
                counter+=1
        return counter
        