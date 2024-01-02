class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr= ''
        for character in s:
            if character.isalnum():
                newstr+=character.lower()
        return newstr==newstr[::-1]

        