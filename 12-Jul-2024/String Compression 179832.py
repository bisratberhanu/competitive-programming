# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        left,ansptr=0,0
        for right in range(1,len(chars)+1):
            if right==len(chars) or chars[right]!=chars[right-1]:
                chars[ansptr]= chars[left]
                ansptr+=1
                print(right-left)
                if right-left>1:
                    for letter in str(right-left):
                        chars[ansptr]=letter
                        ansptr+=1
                left=right
        return ansptr
