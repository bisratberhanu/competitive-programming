class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minword= strs[0]
        for word in strs:
            if len(minword)> len(word):
                minword= word
        common_prefix=''
        for i in range(len(minword)):
            for word in strs:
                if word[i]!= minword[i]:
                    return common_prefix
            common_prefix+=minword[i]
                
        return common_prefix