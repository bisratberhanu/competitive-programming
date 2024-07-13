# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            
            if sorted_str not in anagrams:
                anagrams[sorted_str] = [s]
            else:
                anagrams[sorted_str].append(s)
        
        return list(anagrams.values())