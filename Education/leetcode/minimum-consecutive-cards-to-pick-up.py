class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen=set()
        left=0
        ans= float(inf)
        for right in range(len(cards)):
            while cards[right] in seen:
                ans= min(ans,right-left+1)
                seen.remove(cards[left])
                left+=1
            seen.add(cards[right])
            
        if ans==float(inf):return -1
        return ans  
        