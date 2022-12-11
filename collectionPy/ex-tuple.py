#https://pynative.com/python-tuple-exercise-with-solutions/
#================explication ====================================
#https://www.w3resource.com/python-exercises/tuple/python-tuple-exercise-13.php

#================= exercice 1 : Reverse the tuple =======================
"""
journal=("achat","vent","banque","caisse","operation divers")
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
t=("hello world")
t={}
for i in range(0,len(journal)):
    t[i]=journal[len(journal)-i-1]
    
print(t)

#-1 it s mean start from the end and move by one step 
#print(journal[::-1])
print(t[::-1])

"""
#=====================exercice 2 : print value 20 ===============================
"""
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
listo=tuple1[1]
print(listo[1])
"""

#====================exercice 3 : creat tuple with single item =======================
#tupleo=(50)
#print(tupleo)

#====================exercice 4 :Unpack the tuple into 4 variables ==================

"""
tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1
print(a,b,c,d)
"""
#Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
lst=tuple1
tuple1=tuple2
tuple2=lst
print("tup1",tuple1)
print("tup2",tuple2)