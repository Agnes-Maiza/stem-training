#try,except in python to catch errors
try:
    div =10/0
    value = int(input("Enter a  number :"))
    print(value)
except ValueError: 
    print("invalid number,Entered")
except ZeroDivisionError:
    print("Divided by Zero")