# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixsum=[0]*(n+2)
        for booking in bookings:
            start,end=booking[0],booking[1]
            prefixsum[start]+= booking[2]
            
            prefixsum[end+1]-= booking[2]
        #now calculating the prefic sum
        for i in range(1,len(prefixsum)):
            prefixsum[i]=prefixsum[i-1]+prefixsum[i]
        return prefixsum[1:n+1]

