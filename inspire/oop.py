from msilib.schema import Class


class person:
    def __init__(self,name,dob,height,weight):
        self.name=name
        self.dob=dob
        self.height=height
        self.weight=weight

    def print_age(self):
        self.age=2022-self.dob
        print(f"You are {self.age} years old")
    def print_bmi(self):
        self.bmi=self.height/self.weight
        print(f"Your bmi is {self.bmi}")

class student(person):
    def __init__(self,name,dob,height,weight,S_class,fav_food):
        super().__init__(self,name,dob,height,weight)
        self.S_class=S_class
        self.fav_food=fav_food
    def print_class(self):
        print(f"You are in class{self.S_class}")


