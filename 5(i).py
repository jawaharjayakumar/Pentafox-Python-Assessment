s1=input()
s2=input()
s3=set(s1)^set(s2)
s=""
for i in s3:
    s+=i
print(s)