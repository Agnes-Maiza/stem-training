# GUI with python
from tkinter import*
root=Tk()
#Create text field space
e=Entry(root,width=50,fg="#EF140D",bg="#0FE597")
e.pack()
e.insert(0, "Enter your name")
#create task function
def myClick():
    Hello="Hello " + e.get()
    My_Label =Label(root,text=Hello)
    My_Label.pack()
#create frame
My_Button = Button(root,text="Enter your name", command=myClick,fg="#00FFFF",bg="#BB22AC")
#pack it--Shove it in window
My_Button.pack()

root.mainloop()