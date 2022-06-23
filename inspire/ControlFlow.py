# if statement
x=5

if x >= 1:
    print("Hey,I'm still here")
    x-=1
    print (x)

print("Done")
#else statememnt
x=10
if x == 10:
        print(x)
else :
    print("Not 10")

#elif to create grading system
grade = int(input("Write students score "))
if grade >= 80 and grade <= 100 :
        print("Student got an A")
elif grade >= 70 and grade < 80 :
        print("Student got an B")
elif grade >= 60 and grade < 70 :
        print("Student got an C")
elif grade >= 50 and grade < 60 :
        print("Student got an D")
elif grade < 50 and grade > 0 :
        print("Student got an E")
else :
    print("Invalid score")
