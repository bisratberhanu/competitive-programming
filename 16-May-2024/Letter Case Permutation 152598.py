# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(idx, temp):
            if len(temp) == len(s):
                ans.append(''.join(temp))
                return
            for i in range(idx, len(s)):
                if s[i].isalpha():
                    temp.append(s[i].lower())
                    backtrack(i + 1, temp)
                    temp.pop()

                    temp.append(s[i].upper())
                    backtrack(i + 1, temp)
                    temp.pop()
                else:
                    temp.append(s[i])
                    backtrack(i + 1, temp)
                    temp.pop()

        backtrack(0, [])
        return ans