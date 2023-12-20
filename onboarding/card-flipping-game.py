class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        dis= set()
        ans=[]
        for i in range(len(backs)):
            if backs[i]==fronts[i]:
                dis.add(backs[i])
            else:
                minm=min(backs[i],fronts[i])
                maxm= max(backs[i],fronts[i])
                if minm in dis:
                    if maxm not in dis:
                        ans.append(maxm)
                else:
                    ans.append(minm)
                    ans.append(maxm)
        ans.sort()
        for val in ans:
            if val not in dis:
                return val
        return 0

        