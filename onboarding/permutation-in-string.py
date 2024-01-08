class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1= Counter(s1)
        dic2=defaultdict(int)
        def contains_permutation(string):
            return Counter(string)==dic1
        left=0
        for right in range(len(s2)):
            if right < len(s1):
                dic2[s2[right]]+=1
                if contains_permutation(s2[left:right+1]):
                    return True
                continue
            left+=1
            if contains_permutation(s2[left:right+1]):
                return True
            
            