class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n= len(deck)
        queue= deque([i for i in range(n)])
        lookup= [None]* n
        t= 0

        while queue:
            top= queue.popleft()
            lookup[top]= t
            t+=1 
            if queue:
                queue.append(queue.popleft())

        ans= [ deck[lookup[i]] for i in range(n)]
        return ans 

