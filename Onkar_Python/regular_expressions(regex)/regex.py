# search

str = 'man sun maop run mat rat'

import re
# search() serachs the entire main string and returns the first occurance of the matching string. -> obj
obj = re.search(r'm\w\w',str)# it will return only first result
if obj:
    print(obj.group())
else:
    print('no match')


# ==========================================
# findall
import re

str = 'man sun maop run mat rat'

lst = re.findall(r'm\w\w', str) # it will return all the matching records
# findall() returns all occurrences of the matching string from the main string -> list
if lst:
    for i in lst:
        print(i)
else:
    print('no match')

# =======

str = 'man 2222 sun 4356645 maop 4566456 56run 5466 5467 mat rat'
# so it is dividing when number occurs it devides ??
import re
lst = re.findall(r'\D+', str)
if lst:
    for i in lst:
        print(i)


#==================

str = 'man 2222 sun 4356645 maop 4566456 56run 5466 5467 mat rat'

import re
lst = re.findall(r'\d+', str)
if lst:
    for i in lst:
        print(i)

# ===========
#match() searches only in the beginning of the main string -> obj -> group
#only searches first character
str = ' 10 rani 232 vani 4545 raju 45 ganesh'

import re

obj = re.match(r'r\w\w\w', str)
if obj:
    print(obj.group())
else:
    print('no match')

# =================
# to find all words starting with 'an' or 'ak'

import re

str = 'anil akhill anant arun arati arundhati abhijit ankur amar'

lst = re.findall(r'a[nk]\w*', str)
if lst:
    for i in lst:
        print(i)
else:
    print('no match')
