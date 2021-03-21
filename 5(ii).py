s1=input()
s2=input()
s=""
for i in s1:
    if i not in s2:
        s+=i
for i in s2:
    if i not in s1:
        s+=i
print(s)