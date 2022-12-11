#https://pynative.com/python-tuple-exercise-with-solutions/

#================= exercice 1 : Reverse the tuple=======================
journal=("achat","vent","banque","caisse","operation divers")
t={}
for i in range(0,len(journal)):
    t[i]=journal[len(journal)-i-1]
    
print(t)