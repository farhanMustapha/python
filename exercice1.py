from tkinter import *



def multiplier():
    N=int(entryNumbre1.get())
    N2=2*N
    entryNumbre2.delete(0,END)
    entryNumbre2.insert(0,N2)


app=Tk()


app.geometry("600x500")
lblnumber1=Label(app,text="entrer la valeur de N").place(x=50,y=50)
entryNumbre1=Entry(app)
entryNumbre1.place(x=200,y=50)

lblnumber2=Label(app,text="multiple de N x 2").place(x=50,y=100)
entryNumbre2=Entry(app)
entryNumbre2.place(x=200,y=100)

buttonValider=Button(app,text="valider",command=multiplier).place(x=280,y=150)

app.mainloop()