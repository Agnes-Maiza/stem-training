#sets
fruit={"orange","mangos","apples"}
print(fruit)
print(fruit)
print(fruit)

#functions
def OutputName(a):
    print("Hi",a)
OutputName("Agnes")

#functions to replace characters in a string
def replace_in(phrase):
    word=" "
    for letter in phrase:
        if letter.lower() in "a,e,i,o,u":
            word= word + "g"
        else:
            word= word+letter
    return word

print(replace_in(input("Enter a phrase:")))

