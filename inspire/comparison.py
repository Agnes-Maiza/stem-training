'''#comparison 1
def great_num(n):
    for x in range(n):
        if x>10:
            print(str(x)+" is Greater Than 10")
        else:
            print(x)
great_num(15)'''

#comparison 2
def comparison(a,b):
    for x in range(b):
        if x>a:
            print(str(x)+" is Greater than A")
        if x==a:
            print(str(x)+" is equal to A")
        if x<a:
            print(str(x)+" is Less than A")
comparison(12,20)