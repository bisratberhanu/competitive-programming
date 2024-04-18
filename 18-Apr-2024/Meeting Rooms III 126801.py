# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        heap =[]
        freerooms=[i for i in range(n)]
        heapify(freerooms)
        freq= defaultdict(int)

        for meeting in meetings:
            while heap and heap[0][0] <= meeting[0]:
                end, room = heappop(heap)
                heappush(freerooms, room)
            
            if freerooms:
                length= heappop(freerooms)
                freq[length]+=1
                
                heappush(heap, (meeting[1], length))
               
                
            else: 
                popped= heappop(heap)
                removed= popped[1]
                if popped[0]>= meeting[0]:

                    
                    heappush(heap, (popped[0]+meeting[1]- meeting[0], removed))  # inserts at the minumum removed time
                else:
                     heappush(heap, (meeting[1], removed))
                freq[removed]+=1

        
        
        curmax= float(-inf)
        ans= float(inf)
        for val in freq:
            if freq[val]> curmax:
                curmax= freq[val]
                ans= val
            elif freq[val]== curmax and val< ans:
                ans= val
        return ans 
             
        



            

        

