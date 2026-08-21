# Multiple inheritance

class Father:
    def height(self):
        print("Height = 6.1ft")

class Mother:
    def color(self):
        print("Color = tan")


class Child(Father, Mother):
    pass


# create an object to child class

ch =Child()
print("Qualities of child class:")
ch.height()
ch.color()