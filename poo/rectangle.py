class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur=longueur
        self.largeur=largeur

monRec=Rectangle(7,5)
def surface():
    s=monRec.largeur*monRec.longueur
    print(s)

def perimetre():
    p=monRec.largeur+monRec.longueur
    print(p)
    
perimetre()
surface()