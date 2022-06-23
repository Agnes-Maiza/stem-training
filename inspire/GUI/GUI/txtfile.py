# GUI with python
from tkinter import*
root=Tk()

#create task function
def myClick():
    My_Label =Label(root,text="Hey!,You clicked me!!")
    My_Label.pack()
#create frame
My_Button = Button(root,text="Click me", command=myClick,fg="#00FFFF",bg="#BB22AC")
#pack it--Shove it in window
My_Button.pack()

root.mainloop()