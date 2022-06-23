"""x=0
while x<=25:
    if x%3==0 and x%5==0 :
        print("foobar")
    elif x%3==0:
        print("foo")
    elif x%5==0:
        print("bar")

    else:
        print(x)
       
    x+=1"""
    
#using a function
def print_nums(n):
    for x in range(n):
        if x%3==0 and x%5==0 :
            print("foobar")
        elif x%3==0 and x%5!=0:
            print("foo")
        elif x%5==0 and x%3!=0:
            print("bar")

        elif x%5!=0 and x%3!=0:
            print(x)
       
print_nums(10)

