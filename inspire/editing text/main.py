'''
OOP
Defining a class and its attributes
Creating instances (objects) of a class
Class methods (functions belonging to a class)
Inheritance & Polymorphism
Method overriding
'''

class Dog:
    def __init__(self,no_of_eyes,color,legs):
        self.no_of_eyes= no_of_eyes
        self.color=color
        self.no_of_legs=legs
    def bark(self):
        print("Woof woof!")
    def fetch(self):
        print("Brings item while panting")
        
german_shepherd=Dog(no_of_eyes=2,color='Grey',legs=4)
dodger=Dog(color='White',no_of_eyes=1,legs=3)
dobberman=Dog(2,'Brown',legs=4)
'''
print(german_shepherd.color,german_shepherd.no_of_eyes)
print(dodger.no_of_eyes,dodger.color)
print(dobberman.color,dobberman.no_of_eyes)
'''

dobberman.color='dark-brown'
print(dobberman.color)
print(dobberman.no_of_eyes)
print(dobberman.no_of_legs)
dobberman.bark()
german_shepherd.fetch()