# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        lengths = []
        for word in words:
            bitmask = 0
            for char in set(word):
                bitmask |= 1 << (ord(char) - ord('a'))
            masks.append(bitmask)
            lengths.append(len(word))
        
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, lengths[i] * lengths[j])
        
        return max_product