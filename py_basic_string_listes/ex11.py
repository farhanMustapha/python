s="python.org"
l=[]
for i in range(0,len(s)):
    if s[i] not in l:
        l.append(s[i])
        print("- number of ", s[i]," in python is :",s.count(s[i]))

        
