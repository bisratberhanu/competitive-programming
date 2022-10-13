
def sortSentence(self,s):
        """
        :type s: str
        :rtype: str
        """
        list1 = s.split(" ")
        list1 = sorted(list1, key=lambda x:int(x[-1]))
        list1 = [x[:-1] for x in list1]
        return " ".join(list1)
    
    