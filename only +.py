a = int(input())
b = int(input())
c = int(input())
total = 0
x = (a, b, c)

for i in x:
	if i > 0:
		total += i

print(total)
