#weight-in ceremony
weight = int(input("Enter you weight: "))

if 0 < weight < 60:
    print("Lightweight")
elif 60 <= weight < 64:
    print("Super lightweight")
elif 64 <= weight < 69:
    print("Welterweight")
else:
    print("Out of range")