class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def helper(arr):
            stack=[] # increasing stack
            ans=[1 for i in range(len(arr))]
            for i in range(len(arr)):
                while stack and stack[-1][1]>= arr[i]:
                    popped= stack.pop()
                    ans[popped[0]]*= i- popped[0]

                if stack:
                    temp= i- stack[-1][0]  
                else: 
                    temp=1+i
                ans[i]*=temp
                stack.append((i,arr[i]))
            while stack:
                popped= stack.pop()
                ans[popped[0]]*= len(arr)- popped[0]
            return ans

        span= helper(arr)
        totsum=0
        for i in range(len(arr)):
            totsum+=  arr[i]* span[i]
        return totsum % (10**9+ 7)


       
