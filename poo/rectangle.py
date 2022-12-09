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

class parallelepipede(Rectangle):
    def __init__(self,longueur,largeur,hauteur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur=hauteur

monPara=parallelepipede(6, 3, 2)

def volume():
     v=monPara.largeur*monPara.longueur*monPara.hauteur
     print(v)

volume()