class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        
        arr= [val for val in palindrome]
        if "a"* len(palindrome)== palindrome:
            arr[-1]= 'b'
            return "".join(arr)
        

        
        for i in range(len(arr)):
            if arr[i]!="a":
                save= [i, arr[i]]
                arr[i]="a"
                
                break
        if arr== arr[::-1]:
            arr[-1]= "b"
            arr[save[0]]= save[1]
        return "".join(arr)
                
                 
                