n=int(input())
s=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
l1=[]
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]==s:
            l1.append(l[i])
            l1.append(l[j])
if(len(l1)>0):
    for i in l1:
        print(i,end=" ")
else:

    print("No Pairs found")