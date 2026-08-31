# pickling -- storin the object into the file.


class pickle_exp:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print('%5d %15s %10.2f' %(self.id , self.name, self.salary))




# f =open('d:/py/xyz.txy' 'r' 4096)
# pickle.load()
