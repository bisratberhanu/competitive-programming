class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count= tickets[k]
        queue= deque(tickets)
        queue[k]= [count,True] 
        ans=0
        while count> 0:
            ans+=1
            popped= queue.popleft()
            if popped== [count,True]:
                popped[0]= popped[0]-1
                count-=1
                queue.append(popped)
            else:
                popped-=1
                if popped!= 0:
                    queue.append(popped)
        return ans 

