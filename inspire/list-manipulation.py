#for loop in python

mangoes = "book"
for i in mangoes: 
 
 print(i)

print("done")
#for loops with lists
words=["I","DID","A"]
for word in words:
    print(word + " !")

#count in python
str="hello guys welcome back to my class"
count=0
for  x in str:
    if(x=='o'):
        count+=1
print("The number of 0's is : ",count)

#removing the characters
str="hello guys welcome back to my class"

for  x in str:
    count=0
    if(x=='l'):
        
        continue
    else:
        print(x)

