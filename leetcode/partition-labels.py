class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_dic= {}
        ans=[]
        for i in range(len(s)):
            index_dic[s[i]]= i
        curmax= 0
        left=0
        for right in range(len(s)):
            curmax= max(curmax, index_dic[s[right]])
            if right == curmax:
                ans.append(right-left+1)
                left= right+1
        return ans