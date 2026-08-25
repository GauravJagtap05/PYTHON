# buffer is temp memory block

f = open('file_locction','w',4096)
chars = input('Enter a string to write to file: ')
f.write(chars)
f.close()