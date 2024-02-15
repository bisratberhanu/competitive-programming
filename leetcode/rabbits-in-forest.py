class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # greedy
        # assuming that every same number belong to the same color 
        ans=0
        freq= defaultdict(int)
        
        for val in answers:
            freq[val]+= 1
            if freq[val]== val+1:
                ans+= val+1
                freq[val]= 0
        for val in freq:
            if freq[val]!=0:
                leftover= val+1
                ans+= leftover
        return ans  
