class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        dic= Counter(words)
        lis=[]
        for key in dic:
            lis.append([key,dic[key]])
        sortedlis= sorted(lis,key= lambda x:x[1], reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sortedlis[i][0])
        
        return ans
        
