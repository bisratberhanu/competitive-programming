n= int(input())
alchol= ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", 
          "TEQUILA", "VODKA", "WHISKEY", "WINE"]
count= 0
for _ in range(n):
    s= input()
    if s.isdigit():
        if int(s)<18:
            count+=1
    else:
        if s in alchol:
            count+=1
print(count)