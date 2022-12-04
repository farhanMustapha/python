from tkinter import *


def action():
    lbl['text']="farnanzoo"

app=Tk()
lbl=Label(app,text="hello")
lbl.pack()
btn=Button(app,text="cliquez ici",command=action)
btn.pack()

app.mainloop()