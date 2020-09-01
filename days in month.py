month = int(input("Enter month in number: "))

if 1 <= month <= 7 and month % 2 != 0 or 8 <= month <= 12 and month % 2 == 0:
    print("Days in month = 31")
elif 4 <= month <= 6 and month % 2 == 0 or 9 <= month <= 11 and month % 2 != 0:
    print("Days in month = 30")
else:
    print("Days in month = 28")