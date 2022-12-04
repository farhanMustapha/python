from tkinter import *


def fermer():
    app.quit()

app=Tk()
app.title("fermer")
app.geometry("500x500")

btn1=Button(app,text="quitter",padx=10,pady=10,command=fermer)


btn1.grid(row=0,column=0)


app.mainloop()