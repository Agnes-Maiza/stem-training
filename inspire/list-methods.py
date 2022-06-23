#list[] manupulation methods
fruits=['apple','orange','banana']
fruits.append('cherry')
print(fruits)
fruits.remove('cherry')
print(fruits)
my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)
print()
print()
fruits_2=['cherry','tomato']
fruits_3=fruits+fruits_2
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)
print()
print(fruits)

print()
#tuple()
fruits_4=('mango','lemon','pears')
print(fruits_4)
print(fruits_4[1])
print()
new_list=list(fruits_4)
new_list.append("tomamto")
fruits_4=tuple(new_list)
print(fruits_4)

print()
print()
#set{}
fruits_4=("apple","oranges","oranges","oranges")
fruits_5={"apple","oranges","oranges","oranges"}
print(fruits_4)
print(fruits_5)

print()
#loop and list

my_list=[1,2,3,4,5,6,7,8,9,10]
for x in my_list:
    print(x)
print()
#other_list=my_list
#print(other_list)

#using  for loop to add elements 
'''other_list=[]
for x in  my_list:
    other_list.append(x)
    
print(other_list)

#shorter version
my_list=[1,2,3,4,5,6,7,8,9,10]
other_list=[x for x in my_list]
print(other_list)

other_list=[]
my_list=[1,2,3,4,5,6,7,8,9,10]
for x in my_list:
    if x%2==0:
        other_list.append(x)
print(other_list)
'''
#lists comperehension
my_list=[1,2,3,4,5,6,7,8,9,10]
other_list=[x for x in my_list if x%2==0]
print(other_list)

