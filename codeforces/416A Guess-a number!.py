n= int(input())
right, left= 2* (10**9), -2* (10**9)
import math
for i in range(n):
    sign, val, flag= input().split()
    
    val= int(val)
    if sign=="<=" and flag== "Y":
        right= min(right, val)
    elif sign== ">=" and flag=="Y":
        left= max(left, val)
    elif sign==">" and flag=="Y":
        left = max(left, val+1)
    elif sign=="<" and flag=="Y":
        right= min(right,val-1)
    
    
    elif sign=="<=" and flag== "N":
        left = max(left, val+1)
    elif sign==">=" and flag== "N":
        right= min(right,val-1)
    elif sign=="<" and flag== "N":
         left= max(left, val)
    elif sign==">" and flag== "N":
        right = min (right, val)

if right >=  left:
    print(math.floor((left+right)/2))
else:
    print("Impossible")
    

