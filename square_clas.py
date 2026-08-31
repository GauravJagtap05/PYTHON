class square:
    def __init__(self, x):
        self.x = x

    def area(self):
        square_area = self.x * self.x
        print("Area of square:", square_area)


class rectangle(square):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        rectangle_area = self.x * self.y
        print("Area of rectangle:", rectangle_area)


r = rectangle(5, 10)
r.area()
#
































class Ayush:
    def __init__(self):
        self.name = 'Ayush'
        self.sname = 'Nagre'
        self.age = 22
        self.city = 'Chh Sambhajinagar'

    def display(self):
        print(f'First name is {self.name} and Last name is {self.sname} , my age is {self.age} and I live in {self.city}')

a1 = Ayush()
a1.display()