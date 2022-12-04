from tkinter import *

def valider():
    #a=entry1.get()
    kk=hh.set("hello "+entry1.get())
    lbl=kk


app=Tk()

app.geometry("500x500")
entry1=Entry(app)
entry1.pack()

btn=Button(app,text="valider",command=valider)
btn.pack()
hh=StringVar()
lbl=Label(app,text="helloooo....",textvariable=hh)
lbl.pack()

app.mainloop()