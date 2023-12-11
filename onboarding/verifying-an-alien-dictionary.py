class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def helper(order):
            return order
            

        #print(sorted(words,key=lambda word: [order.index(c) for c in word]))
        return sorted(words,key=lambda word: [order.index(c) for c in word])== words

        