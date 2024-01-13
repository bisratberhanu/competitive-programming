class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):return ''
        dic_t= Counter(t)
        #print(dic_t)
        ans=''
        left=0
        dic= defaultdict(int)
        def checker(dic,dic_t):
            for val in dic_t:
                if val not in dic or dic[val]< dic_t[val]:
                    return False
            return True
        for right in range(len(s)):
            dic[s[right]]+=1
            while checker(dic,dic_t):
                if ans=='' or len(ans)> len(s[left:right+1]):
                    ans= s[left:right+1]
                    #print(ans)
                dic[s[left]]-=1
                if dic[s[left]]==0: del dic[s[left]]
                print(left)
                left+=1
        return ans 
        