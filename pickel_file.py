# pickling

import pickle , Reading_Files

f = open("d:/emp_data" , 'wb' , 4096)
n = int(input(" how many employees "))

for i in range(n):
    id = int(input(" enter id : "))
    name = input(" enter name : ")
    salary = float(input(" enter salary : "))

e = Reading_Files.pickle_exp(id,name,salary)
pickle.dump(e,f)



