#removing the characters(Verticaly)
str="hello guys welcome back to my class"
print("hello guys welcome back to my\n\n class")

for  x in str:
    if x !='l':
        print(x)

#removing the characters(horizontaly)
str="hello guys welcome back to my class"
outstr= ""
for  x in str:
    if x !='l' and x !='e' and x !='u' :
        outstr+=x
print()        
print(outstr)
print("1.hello 2.guys 3.welcome 4.back 5.to my class")
print()
print("1.hello \n2.guys \n3.welcome \n4.back \n5.to my class")
#
for i in range(1,100,2):
    print(i)