while(1):
    #try
    try:
        x=int(input("Please enter the first number: "))
        y=int(input("Please enter the second number: "))
        z=x/y
    #except
    except ZeroDivisionError:
        print("Cannot divide by zero")
        continue
    except ValueError:
        print("You did not enter an integer")
        continue
    #else
    else: 
        print(z)
        break
    #finally
    finally:
        print("This program ends here")


