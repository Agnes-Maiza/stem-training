#x="qwertyuio"
#print(x[:4])
# GUI with python
from tkinter import*
root=Tk()
#Create text field space
e=Entry(root,width=50,fg="white",bg="red")
e.pack()
e.insert(0, "Enter first no")

#create task function
def myClick():
    str_=e.get()
    if "*" in str_:
        y=str_.index("*")
        f_no= float(str_[:y])
        s_no= float(str_[(y+1):])
        mult=f_no * s_no
        ans="multiplication: "+str(mult)
        My_Label =Label(root,text=ans)
        My_Label.pack()
#create frame
My_Button = Button(root,text="=", command=myClick,fg="#00FFFF",bg="#BB22AC")
#pack it--Shove it in window
My_Button.pack()

root.mainloop()