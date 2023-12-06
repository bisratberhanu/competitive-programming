class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        row1 = "qwertyuiop"
        row2= "asdfghjkl"
        row3= "zxcvbnm"
        for word in words:
            counter1,counter2,counter3=0,0,0
            for letter in word:
                if letter.lower() in row1:
                    counter1+=1
                elif letter.lower() in row2:
                    counter2+=1
                else: counter3+=1
            if counter1== len(word) or counter2==len(word) or counter3==len(word):
                ans.append(word)
        return ans 
            