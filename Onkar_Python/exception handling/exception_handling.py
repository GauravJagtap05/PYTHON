try:
    print("Open the file")

    a = int(input("enter a number: "))
    b = int(input("enter another number: "))

    c = a / b

    print("result =", c)

except ZeroDivisionError as e:
    print("Error:", e)

finally:
    print("close the file")

# when  you dont know the error

try:
    print("Open the file")

    a = int(input("enter a number: "))
    b = int(input("enter another number: "))

    c = a / b

    print("result =", c)

except Exception as e:
    print(e)
finally:
    print("close the file")

