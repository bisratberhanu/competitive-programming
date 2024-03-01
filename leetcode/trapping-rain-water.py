class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[0]
        maxright=[0]* len(height)

        maxl, maxr=0,0
        for i in range(1,len(height)):
            maxl=max(maxl, height[i-1]) 
            maxleft.append(maxl)
        for i in range(len(height)-2,-1,-1):
            maxr=max(maxr, height[i+1])
            maxright[i]= maxr
        ans=0
        

        for i in range(len(height)):
            temp= min( maxright[i], maxleft[i])- height[i]
            if temp>0:
                ans+=temp
            
        return ans 

            