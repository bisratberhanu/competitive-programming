class Solution:
    def minimizedStringLength(self, s: str) -> int:
        not_repeated=set()
        for letter in s:
            not_repeated.add(letter)
        return len(not_repeated)