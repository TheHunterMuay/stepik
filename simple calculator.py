a1 = int(input("First digit: "))
a2 = int(input("Second digit: "))
z = str(input( "Enter +,-,/,* : "))

if (a1 == 0 or a2 == 0) and z == "/":
    print("Division by zero is undefined!")
elif (a1 > 0 and a2 > 0) and z == "+":
    print(a1 + a2)
elif (a1 > 0 and a2 > 0) and z == "-":
    print(a1 - a2)
elif (a1 > 0 and a2 > 0) and z == "*":
    print(a1 * a2)
elif (a1 > 0 or a2 > 0) and z == "/":
    print(int(a1 / a2))
else:
    print("Wrong operation")