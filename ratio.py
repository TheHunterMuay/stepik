num = int(input("Enter 4th digit number: "))
a = (num % 10 ** 4) // 10 ** (4 - 1) #1st digit
b = (num % 10 ** (4 - 1)) // 10 ** (4 - 2) #2nd digit
c = (num % 10 ** (4 - 2)) // 10 ** (4 - 3) #3rd digit
d = (num % 10 ** (4 - 3)) // 10 ** (4 - 4) #4th digit


	
if a + d == b - c:
	print("YES")
else:
	print("NO")









