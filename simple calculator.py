a1 = int(input("First digit: "))
a2 = int(input("Second digit: "))
z = str(input( "Enter +,-,/,* : "))


if z == "+":
    print(a1 + a2)
elif z == "-":
    print(a1 - a2)
elif z == "*":
    print(a1 * a2)
elif a2 > 0 and z == "/":
    print (a1 / a2)
elif a2 == 0 and z == "/":
    print("Division by zero is undefined!")
else:
    print("Wrong operation")
