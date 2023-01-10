
#===programme permet de donner l'extention du fichier =======
#===================== ex 01 =============================
fichier=input("saisire le nom du fichier :")
l=fichier.split(" ")
print(l)
if(l[1]=="pdf"):
    print("the extention is ",l[1])
if(l[1]=="xlsx"):
    print("the extention is ",l[1])
if(l[1]=="csv"):
    print("the extention is ",l[1])
if(l[1]=="txt"):
    print("the extention is ",l[1])
else:
    print("your file has no extention")