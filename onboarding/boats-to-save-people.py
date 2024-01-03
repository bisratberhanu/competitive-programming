class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans,left,right=0,0,len(people)-1
        while left<=right:
            if left==right:
                ans+=1
                return ans 
            if people[left]+people[right]<=limit:
                ans+=1
                left+=1
                right-=1
            else:
                ans+=1
                right-=1
        return ans 