from tkinter import *

def validate():
    ttc=int(entryTtc.get())
    ht=ttc/1.2
    tva=ht*0.2
    entryHt.insert(0,ht)
    entryTva.insert(0,tva)

app=Tk()
app.geometry("600x500")

entryDate=Entry(app).place(x=50,y=10)
entryCpt=Entry(app).place(x=200,y=10)
entryDescription=Entry(app).place(x=50,y=70)


lbl=Label(app,text="entrer ttc:").place(x=50,y=100)
entryTtc=Entry(app)
entryTtc.place(x=150,y=100)

entryHt=Entry(app)
entryHt.place(x=150,y=200)

entryTva=Entry(app)
entryTva.place(x=150,y=300)



btnValider=Button(app,text="valider",command=validate).place(x=50,y=250)


app.mainloop()