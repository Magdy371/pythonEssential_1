#Commom year and leap year
year_number = int(input("Enter a year: "))
if year_number < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year_number % 4 != 0:
        print("Common year")
    elif year_number % 100 != 0:
        print("Leap year")
    elif year_number % 400 != 0:
        print("Common year")
    else:
        print("Leap year")