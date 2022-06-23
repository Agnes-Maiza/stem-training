# oop= object-oriented programming

# Defining a class and its attributes
class dog:
    def __init__(self,no_of_eyes,color,gender):
       self.no_of_eyes = no_of_eyes
       self.color = color
       self.gender=gender
    # Class methods (functions belonging to a class)
    def bark(self):
        print("woof! woof!")
    def reproduce(self):
        print("externally")

# Creating instances(objects) of a class
german_shepherd = dog(no_of_eyes=2,color="grey",gender="male")
dodger=dog(no_of_eyes=1,color="white",gender="female")
dobberman=dog(2,"brown","male")


print(german_shepherd.color,german_shepherd.no_of_eyes,german_shepherd.gender)
print(dodger.no_of_eyes,dodger.color,dodger.gender)
print(dobberman.no_of_eyes,dobberman.color,dobberman.gender)
dobberman.bark()
print(dobberman.gender)
print(german_shepherd.gender)
print(dodger.gender)
german_shepherd.reproduce()

dobberman.color="dark-brown"
print(dobberman.color)

