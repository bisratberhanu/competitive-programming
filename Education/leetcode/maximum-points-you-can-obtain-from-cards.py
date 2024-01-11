class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxsum= sum(cardPoints)
        left=0
        ans= float(-inf)
        currsum=0
        sliding= len(cardPoints)-k # the lenght of our sliding window 
        for right in range(len(cardPoints)):
            currsum+=cardPoints[right]
            if right < sliding:
                if right==sliding-1:
                    ans= max(ans,maxsum-currsum)
                continue
            currsum-=cardPoints[left]
            left+=1
            ans= max(ans, maxsum-currsum)
        return ans 
            

