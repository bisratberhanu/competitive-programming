class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans=0
        left,right= 0, len(skill)-1
        checker= skill[right]+skill[left]
        while left<right:
            chemistry= skill[left]+skill[right]
            if chemistry!=checker:
                return -1
            ans+= skill[left]*skill[right]
            left+=1
            right-=1
        return ans 
        