class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_blocks=0
        left=0
        ans= float('inf')
        for right in range(len(blocks)):
            if right< k:
                if blocks[right]=='W':
                    white_blocks+=1
                if right==k-1:
                    
                    ans= min(ans,white_blocks) 
            else:
                if blocks[left]=='W':
                    white_blocks-=1
                if blocks[right]=='W':
                    white_blocks+=1
                ans= min(ans,white_blocks)
                left+=1
            #print(ans)
            #print(white_blocks)
        ans= min(ans,white_blocks)
        return ans 
