s=list(map(int,input().split(',')))
l=[]
s1=""
for i in s:
    i+=64
    l.append(i)
for i in l:
    s1+=chr(i)
print(s1)