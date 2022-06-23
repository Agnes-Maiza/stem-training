#dictionaries inpython
mydict={
    "Book":"Dynamics",
    "Publisher":"Longhorn",
    "Year":2001

}
#Accessing item
x=mydict["Year"]
print(x)
#Accessing using get()
y=mydict.get("Book")
print(y)
#All keys
x=mydict.keys()
print(x)

#All values
x=mydict.values()
print(x)

#Printing all items in a dictionary
x=mydict.items()
print(x)
#checking if keys exists
if "Publisher" in mydict:
    print("Publisher is one of your the keys")
#length of a dictionary
print(len(mydict))

#dictionaries that can hold different data types
mydict={
    "Book":"Dynamics",
    "Publisher":"Longhorn",
    "Year":2001,
    "Authors":["John","Mike","ike"]

}
s=mydict["Authors"]
print(s)
