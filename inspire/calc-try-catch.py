#complex calculator
x=input("Enter the first value ")
y=input("Enter the second value ")
p=input("Enter an operator.(eg +,-,*,/,%) ")
try:
    if p == '+':
        result= int (x)+int (y)
        print(x,p,y,"=",result)
    elif p == '-':
        result= int (x)-int (y)
        print(x,p,y,"=",result)
    elif p == '*':
        result= int (x)*int (y)
        print(x,p,y,"=",result)
    elif p == '/':
        result= int (x)/int (y)
        print(x,p,y,"=",result)
    elif p == '%':
    
        result= int (x)%int (y)
        print(x,p,y,"=",result)
    else :
        print("Invalid operator")

except ValueError: 
    print("invalid number,Entered")
except ZeroDivisionError:
    print("Divided by Zero")


