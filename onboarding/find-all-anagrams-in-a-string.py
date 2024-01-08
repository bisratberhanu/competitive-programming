class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        dict_of_p= Counter(p)
        def isanagram(string):
            return Counter(string)==dict_of_p
        
        
        left,right=0, len(p)-1
        
        
        
        while right< len(s):
            if isanagram(s[left:right+1]):
                ans.append(left)
            left+=1
            right+=1
        return ans 

        