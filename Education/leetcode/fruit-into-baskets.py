class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen=defaultdict(int)
        ans=float(-inf)
        left=0
        for right in range(len(fruits)):
            while fruits[right] not in seen and len(seen)==2:
                seen[fruits[left]]-=1
                if seen[fruits[left]]==0: del seen[fruits[left]]
                left+=1
            seen[fruits[right]]+=1
            ans= max(ans, sum(seen.values()))
        return ans 
        