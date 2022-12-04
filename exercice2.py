from tkinter import *

def validate():
    print("hellooooooooo")
    n=int(entryNumber.get())
    lblRslt['text']="diviseur de n: "
    for i in range(1,n+1):
        if(n%i==0):
            lblRslt['text']=lblRslt['text']+" " +str(i)+" "

app=Tk()
app.geometry("600x500")

lbl=Label(app,text="entrer a number :").place(x=50,y=100)
entryNumber=Entry(app)
entryNumber.place(x=150,y=100)
lblRslt=Label(app,text="result is:")
lblRslt.place(x=50,y=200)

btnValider=Button(app,text="valider",command=validate).place(x=50,y=250)


app.mainloop()