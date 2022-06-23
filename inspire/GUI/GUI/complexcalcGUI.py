# GUI with python
from tkinter import*
root=Tk()
#Create text field space
e1=Entry(root,width=50,fg="white",bg="red")
e1.pack()
e1.insert(0, "Enter first no")
#Create text field space(second input)
e2=Entry(root,width=50,fg="#EF140D",bg="#0FE597")
e2.pack()
e2.insert(0, "Enter second no")
#create task function
def myClick():
    f_no = float(e1.get())
    s_no=float(e2.get())
    sub=f_no - s_no
    add=f_no + s_no
    div=f_no / s_no
    mult=f_no * s_no
    ans="Addition: "+ str(add) + "\nsub: "+str(sub) + "\ndivision: "+ str(div) + "\nmultiplication: "+str(mult) 
    My_Label =Label(root,text=ans)
    My_Label.pack()
#create frame
My_Button = Button(root,text="=", command=myClick,fg="#00FFFF",bg="#BB22AC")
#pack it--Shove it in window
My_Button.pack()

root.mainloop()