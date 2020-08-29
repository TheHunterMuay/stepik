a = int(input('Side "A"'))
b = int(input('Side "B"'))
c = int(input('Side "C"'))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print("YES")
else:
    print("NO")