a= input()
b= input()
inta= int(a)
intb= int(b)
val1= str(inta+intb)
str1,str2,str3="", "", ""
for letter in a:
    if letter!="0":
        str1+= letter
for letter in b:
    if letter!="0":
        str2+= letter
for letter in val1:
    if letter!="0":
        str3+= letter

val2= int(str1)+int(str2)
if int(val2)== int(str3):
    print("YES")
else: print("NO")


