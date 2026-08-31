# Multiple inheritance

class father:
    def height(self):
        print("height of father = 6.1 ft")

class mother:
    def colour(self):
        print(" clour : tan")

class child(father,mother):
    def qualifications(self):
        print(" qualification = Engineer")


# create an object to an child class

obj = child()
print("qualitites of child")
obj.height()
obj.colour()
obj.qualifications()

