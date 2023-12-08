class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic= defaultdict(list)
        for pair in matches:
            dic[pair[0]]=[0,0]
            dic[pair[1]]= [0,0]
        for pair in matches:
            winner,loser= pair[0], pair[1]
            dic[winner][0]+=1
            dic[loser][1]+=1

        winners,loser_1=[],[]
        for val in dic:
            if dic[val][1]==0:
                winners.append(val)
            if dic[val][1]==1:
                loser_1.append(val)
        
        winners.sort()
        loser_1.sort()
        ans=[]
        ans.append(winners)
        ans.append(loser_1)
        return ans
