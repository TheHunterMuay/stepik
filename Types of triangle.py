x = int(input("Enter 1st side: " ))
y = int(input("Enter 2nd side: " ))
z = int(input("Enter 3rd side: " ))

if x == y == z:
    print("Equilateral")
elif x == y != z or x != y == z or x == z != y:
    print("Isosceles")
else:
    print("Scalene")

