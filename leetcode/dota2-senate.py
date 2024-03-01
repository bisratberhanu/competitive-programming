class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire, radiant, n= deque(), deque(), len(senate)
        for i in range(len(senate)):
            if senate[i]== "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            rad_idx= radiant.popleft()
            dire_idx= dire.popleft()
            if rad_idx< dire_idx:
                radiant.append(rad_idx+n)
            else:
                dire.append(dire_idx+n)
        
        if radiant: return "Radiant"
        return "Dire"
