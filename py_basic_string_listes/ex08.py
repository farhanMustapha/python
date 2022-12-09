#diviseur de n
n=int(input("tapez un nombre n : "))
for i in range(1,n):
    if n%i==0:
        print(i ,"is diviseur de n")
