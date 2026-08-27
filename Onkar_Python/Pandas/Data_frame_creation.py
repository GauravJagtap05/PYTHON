# data frame creation 

#====================

# csv file

import pandas as pd

df = pd.read_csv("/Users/onkar/Downloads/datasets1/empdata.csv")

print(df)
# %%


#====================

# excel file


df = pd.read_excel('/Users/onkar/Downloads/datasets1/empdata.xlsx',
    sheet_name='sheet1'
)

print(df)


#====================
# %%


# tab file

df = pd.read_table(
    '/Users/onkar/Downloads/datasets1/textdata.txt',
    names=('a', 'b', 'c', 'Person'),
    sep=r'\s+')

print(df)

#====================


# python dictoinry
# %%



empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
"ename": ["Ganesh Rao", "Anil Kumar", "Gaurav Gupta", "Hema Chandra", "Laxmi Prasanna", "Anant Nag"],
"sal": [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99],
"doj": ["10-10-2000", "3-20-2002", "3-3-2002", "9-10-2000", "10-8-2000", "9-9-1999"]}

df = pd.DataFrame(empdata)
print(df)
#====================
# %%
#====================

# tupples

# python list of tuples

empdata = [(1001, 'Ganesh Rao', 10000.00, '10-10-2000'),
(1002, 'Anil Kumar', 23000.50, '3-20-2002'),
(1003, 'Gaurav Gupta', 18000.33, '03-03-2002'),
(1004, 'Hema Chandra', 16500.50, '10-09-2000'),
(1005, 'Laxmi Prasanna', 12000.75, '08-10-2000'),
(1006, 'Anant Nag', 9999.99, '09-09-1999')]

df = pd.DataFrame(empdata, columns =['eno','ename','sal','doj'])
print(df)

#====================
# %%


#====================


#====================


#====================


#====================

#====================

#====================


#====================


#====================


#===================
# ===

df = pd.read_csv('/Users/onkar/Downloads/datasets1/')

df.loc[:,'ename']

df.iloc[:,1]

df.loc[:,['ename','doj']]

df.iloc[:,[1,3]]

df.iloc[2:3,:]

df.loc[2:3,:]

# %%