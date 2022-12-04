from tkinter import *

app=Tk()
app.title("button")
app.geometry("500x500")

btn1=Button(app,text="Button 1",padx=10,pady=10)
btn2=Button(app,text="Button 2",padx=10,pady=10)
btn3=Button(app,text="Button 3",padx=10,pady=10)
btn4=Button(app,text="Button 4",padx=10,pady=10)

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=1,column=0)
btn4.grid(row=1,column=1)


app.mainloop()