class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        ans= [0]* n
        stack=[]
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped_idx= stack.pop()
                ans[popped_idx]= i- popped_idx
            
            stack.append(i)
        return ans 
