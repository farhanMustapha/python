a=[1,8,10,15,30]
b=[11,18,22,15,40]
c=[]
for i in a:
    for j in b:
        l1=a[i]
        l2=b[j]
        if l2>l1:
            c[i]=l2

print(c)            