class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic= {2: "abc", 3:"def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8:"tuv", 9: "wxyz"}
        ans=[]
        def backTrack(index, lis):
            if len(digits)==0:
                return
            if len(lis)== len(digits):
                ans.append("".join(lis))
                return
            
            
            for val in dic[int(digits[index])]:
                lis.append(val)
                backTrack(index+1, lis)
                lis.pop()
        
        backTrack(0,[])

        return ans 
            